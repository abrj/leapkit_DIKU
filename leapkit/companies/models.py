import uuid
import StringIO

import re
from django.core.mail import EmailMessage
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as Img
from geographic_info.models import Region, Country
from projects.models import Project
from leapkit import settings


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('companies/logos/', filename)


class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Industry"
        verbose_name_plural = "Industries"


class Company(models.Model):
    # Basic information
    user = models.OneToOneField(User, unique=True, blank=True)
    name = models.CharField(max_length=254,
                            help_text="Please write the name of you company.")
    times_logged_in = models.IntegerField(default=1)

    # Geographic information
    country = models.ForeignKey(Country,
                                related_name="company_country",
                                null=True,
                                blank=True,
                                help_text="Please choose country in which your company is registered.")

    region = models.ForeignKey(Region,
                               related_name="company_region",
                               null=True,
                               blank=True,
                               help_text="Please choose the region in which you company is registered.")

    address = models.CharField(max_length=254, blank=True)

    company_size = models.IntegerField(null=True, blank=True,
                                       help_text="Please give an estimation of the size of your company.")
    year_founded = models.IntegerField(null=True, blank=True,
                                       help_text="Please provide the year your company was founded.")
    website = models.URLField(blank=True,
                              help_text="Please provide the URL of your company website. "
                                        "Make sure the URL begins with 'http://'")
    date_joined = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(max_length=255,
                            unique=True,
                            blank=True)

    logo = models.ImageField(upload_to=get_file_path,
                             blank=True,
                             help_text="Please choose an logo of your company logo.")

    # General information
    industry = models.ForeignKey(Industry,
                                 help_text="Please select the company's primary industry.")
    about = models.TextField(blank=True,
                             help_text="Please write what your company's business is about.")
    overview = models.TextField(blank=True,
                                help_text="Please write a short overview of your company.")
    mission = models.TextField(blank=True,
                               help_text="please write the mission of your company.")

    # Projects information
    projects_available = models.IntegerField(default=0, blank=True)
    projects_latest_buying_date = models.DateField(blank=True, null=True)
    projects_former_buying_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.name

    def get_absolute_update_url(self):
        return reverse('companies:update_profile', kwargs={'pk': self.pk})

    @models.permalink
    def get_absolute_url(self):
        return reverse('companies:profile', kwargs={'slug': self.slug, })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.unique_slugify(self.name)

        width = 250
        height = 250
        size = (width, height)
        is_same = False
        if self.logo:
            try:
                this = Company.objects.get(id=self.id)
                if this.photo == self.logo:
                    is_same = True
            except:
                pass  # when new photo then we do nothing, normal case

            logo = Img.open(StringIO.StringIO(self.logo.read()))
            (imw, imh) = logo.size
            if (imw > width) or (imh > height):
                logo.thumbnail(size, Img.ANTIALIAS)

            # If RGBA, convert transparency
            if logo.mode == "RGBA":
                logo.load()
                background = Img.new("RGB", logo.size, (255, 255, 255))
                background.paste(logo, mask=logo.split()[3])  # 3 is the alpha channel
                logo = background

            output = StringIO.StringIO()
            logo.save(output, format='JPEG', quality=60)
            output.seek(0)
            self.logo = InMemoryUploadedFile(output, 'logoField', "%s.jpg" % self.logo.name.split('.')[0],
                                             'logo/jpeg', output.len, None)

        try:
            this = Company.objects.get(id=self.id)
            if this.logo == self.logo or is_same:
                self.logo = this.logo
            else:
                this.logo.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case

        super(Company, self).save(*args, **kwargs)

    def send_activation_email(self):
        subject = "Thank you for registering at Leapkit.com"

        email = "Hi %s \n\n " \
                "Welcome to the Leapkit.com! \n" \
                " We are happy to have you on board! \n" \
                "We really hope that you can use the platform! \n" \
                "We have been working hard to get to this point, but there is still a long way to go. \n" \
                "If you encounter any problems, or can think of features that would improve your experience, " \
                "do not hesitate contacting us! \n\n We appreciate all feedback, both positive and negative! \n\n" \
                "You can get a hold on us via email at contact@leapkit.com! \n\n\n" \
                "Best regards\n" \
                "Leapkit team" % (self.get_full_name())

        email = EmailMessage(subject=subject,
                             body=email,
                             from_email=settings.DEFAULT_FROM_EMAIL,
                             to=[self.user.email, ])
        email.send()



    # TODO test this code found online
    def _slug_strip(self,
                    value,
                    separator='-'):
        """
        Cleans up a slug by removing slug separator characters that occur at the
        beginning or end of a slug.

        If an alternate separator is used, it will also replace any instances of
        the default '-' separator with the new separator.
        """
        separator = separator or ''
        if separator == '-' or not separator:
            re_sep = '-'
        else:
            re_sep = '(?:-|%s)' % re.escape(separator)
        # Remove multiple instances and if an alternate separator is provided,
        # replace the default '-' separator.
        if separator != re_sep:
            value = re.sub('%s+' % re_sep, separator, value)
        # Remove separator from the beginning and end of the slug.
        if separator:
            if separator != '-':
                re_sep = re.escape(separator)
            value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
        return value

        # TODO implement the unique_slugify so the slug can be used as user url.
        # def unique_slugify(self):
        # slug = slugify(self.name)
        #
        # user = CustomUser.objects.get(slug=slug)
        #
        # while user is not None:
        # slug += "-%i" % random.randint(1,2000)
        # user = CustomUser.objects.get(slug=slug)
        #
        #     self.slug = slug

        # TODO test this code found online

    def unique_slugify(instance,
                       value,
                       slug_field_name='slug',
                       queryset=None,
                       slug_separator='-'):
        """
        Calculates and stores a unique slug of ``value`` for an instance.

        ``slug_field_name`` should be a string matching the name of the field to
        store the slug in (and the field to check against for uniqueness).

        ``queryset`` usually doesn't need to be explicitly provided - it'll default
        to using the ``.all()`` queryset from the model's default manager.
        """
        slug_field = instance._meta.get_field(slug_field_name)

        slug = getattr(instance, slug_field.attname)
        slug_len = slug_field.max_length

        # Sort out the initial slug, limiting its length if necessary.
        slug = slugify(value)
        if slug_len:
            slug = slug[:slug_len]
        slug = instance._slug_strip(slug, slug_separator)
        original_slug = slug

        # Create the queryset if one wasn't explicitly provided and exclude the
        # current instance from the queryset.
        if queryset is None:
            queryset = instance.__class__._default_manager.all()
        if instance.pk:
            queryset = queryset.exclude(pk=instance.pk)

        # Find a unique slug. If one matches, at '-2' to the end and try again
        # (then '-3', etc).
        next_element = 2
        while not slug or queryset.filter(**{slug_field_name: slug}):
            slug = original_slug
            end = '%s%s' % (slug_separator, next_element)
            if slug_len and len(slug) + len(end) > slug_len:
                slug = slug[:slug_len - len(end)]
                slug = instance._slug_strip(slug, slug_separator)
            slug = '%s%s' % (slug, end)
            next_element += 1

        setattr(instance, slug_field.attname, slug)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class CompanyProjectManager(models.Manager):
    def get_own_projects(self, user):
        projects = super(CompanyProjectManager, self).get_queryset().filter(is_active=True, project_owner=user)
        return projects

    def get_published_queryset(self):
        projects = super(CompanyProjectManager, self).get_queryset().filter(is_active=True, published=True)
        return projects

    def get_own_published_queryset(self, user):
        projects = super(CompanyProjectManager, self).get_queryset().filter(is_active=True,
                                                                            published=True,
                                                                            project_owner=user)
        return projects

    def get_own_drafts_queryset(self, user):
        projects = super(CompanyProjectManager, self).get_queryset().filter(is_active=True,
                                                                            published=False,
                                                                            project_owner=user)
        return projects


class CompanyProject(Project):
    """
    This model is to be used for all projects created by companies.
    It contains all the fields needed to create an advanced company project.
    """

    project_owner = models.ForeignKey(Company)
    payment = models.CharField(max_length=2,
                               blank=True,
                               choices={("P", "Paid"), ("NP", "Not Paid")},
                               help_text="Please choose if the work is paid or not.")

    web_page = models.URLField(blank=True,
                               help_text="Please provide the URL to a relevant website. "
                                         "Make sure the URL begins with 'http://'")

    involvement = models.IntegerField(verbose_name="Estimated involvement time pr. month (In hours)",
                                      help_text="Please estimate how much time will be used internally "
                                                "on this project, hands on with the students")

    COURSE = "C"
    BACHELOR_THESIS = "B"
    MATER_THESIS = "M"
    INTERN = "I"
    All = "A"
    BACHELOR_THESIS_AND_MASTER_THESIS = "BM"

    WORKLOAD = {
        (COURSE, "Course Project"),
        (BACHELOR_THESIS, "Bachelor Thesis"),
        (MATER_THESIS, "Master Thesis"),
        (INTERN, "Internship"),
        (BACHELOR_THESIS_AND_MASTER_THESIS, "Bachelor & Master Thesis"),
        (All, "ALL")
    }

    thesis_or_internship_required = models.CharField(max_length=2,
                                                     blank=True,
                                                     choices=WORKLOAD,
                                                     default=All,
                                                     help_text="Please select if your project is only suitable "
                                                               "for students using it as basis for their bachelor, "
                                                               "master thesis or educational internship")

    nda_required = models.CharField(max_length=2,
                                    blank=True,
                                    choices={("Y", "Yes"), ("N", "No")},
                                    help_text="If your project involves highly sensitive information, "
                                              "you can demand that the Companys sign a non-disclosure agreement (NDA), "
                                              "which protects your IP. We provide a standard NDA approved by "
                                              "IP-lawyers and university professors.")

    resume_required = models.CharField(max_length=1,
                                       blank=True,
                                       choices={("Y", "Yes"), ("N", "No")},
                                       help_text="Please choose if the student is required "
                                                 "to attach a resume when contacting you")

    objects = CompanyProjectManager()


class ProjectPackage(models.Model):
    company_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=254,
                               blank=True)

    START_UP = "SU"
    STANDARD = "ST"
    ENTERPRISE = "EN"

    TYPE = {
        (START_UP, "Start-Up"),
        (STANDARD, "Standard"),
        (ENTERPRISE, "Enterprise")
    }

    type = models.CharField(max_length=2,
                            choices=TYPE)

    buying_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    invoice_sent = models.BooleanField(default=False)
    payment_received = models.BooleanField(default=False)
    note = models.TextField(blank=True)

    def __unicode__(self):
        return self.company_name


