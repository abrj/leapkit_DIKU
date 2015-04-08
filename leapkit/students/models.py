import uuid
import StringIO

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import models
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile
import re
import os
from PIL import Image as Img
from rest_framework.reverse import reverse
from institutions.models import Institution, Department, Course, FieldOfStudy
from geographic_info.models import City, Region, ZipCode, Street, Country
from projects.models import Project
from leapkit import settings



def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('students/profile_images/', filename)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('students/project_files/', filename)


class Student(models.Model):
    # Instantiating options
    MALE = "M"
    FEMALE = "F"

    SEX = {
        (MALE, "Male"),
        (FEMALE, "Female"),
    }

    # Basic information
    user = models.OneToOneField(User, unique=True, blank=True)
    image = models.ImageField(upload_to=get_image_path,
                              blank=True,
                              help_text="Please choose an image of yourself to upload and show to other users.")
    times_logged_in = models.IntegerField(default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField(null=True,
                                     blank=True,
                                     help_text="Please select your date of birth.")
    gender = models.CharField(max_length=1,
                              choices=SEX,
                              blank=True,
                              help_text="Please select your gender.")

    # Practical information
    date_joined = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    BACHELOR = "BSC"
    MASTER = "MSC"
    EDUCTATION_LEVEL = {
        (BACHELOR, "Bachelor Student"),
        (MASTER, "Master Student")
    }
    education_level = models.CharField(max_length=3,
                                       choices=EDUCTATION_LEVEL,
                                       blank=True,
                                       help_text="Please select your current education level")
    # Geographic information
    country = models.ForeignKey(Country,
                                related_name="student_country",
                                null=True,
                                blank=True,
                                help_text="Please select the country in which you are currently living.")

    region = models.ForeignKey(Region,
                               related_name="student_region",
                               null=True,
                               blank=True,
                               help_text="Please select the region in which you are currently living.")

    zip_code = models.ForeignKey(ZipCode,
                                 related_name="student_zipcode",
                                 null=True,
                                 blank=True,
                                 help_text="Please provide your current zip_code.")

    city = models.ForeignKey(City,
                             related_name="student_city",
                             null=True,
                             blank=True,
                             help_text="Please provide the city in which you are currently living.")

    street = models.ForeignKey(Street,
                               related_name="student_street",
                               null=True,
                               blank=True,
                               help_text="Please provide the name of your street.")

    # Educational information
    institution = models.ForeignKey(Institution,
                                    help_text="Please select the institution providing your education.")

    department = models.ForeignKey(Department,
                                   null=True,
                                   blank=True,
                                   help_text="Please select the department in which you belong.")

    courses = models.ManyToManyField(Course,
                                     null=True,
                                     blank=True,
                                     help_text="Please select the courses you are currently attending.")

    line_of_study = models.ForeignKey(FieldOfStudy,
                                           null=True,
                                           blank=True,
                                           help_text="Please select the interests you would like to use in projects.")

    # Personal information
    description = models.TextField(blank=True,
                                   help_text="Please write a personal description.")

    cv = models.FileField(upload_to=get_file_path,
                          blank=True,
                          help_text="Please choose an file of your choice to upload and show to other users.")

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_full_name(self):
        """
        :return: First name + last name, with a space in between
        """
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        """
        :return: email
        """
        return self.first_name

    def get_absolute_update_url(self):
        return reverse('students:update_profile', kwargs={'slug': self.slug})

    # TODO implement a way to lead directly to the users profile via. the get_absolute_url
    @models.permalink
    def get_absolute_url(self):
        return reverse("students:profile", args=(self.slug, ))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.unique_slugify(value="%s %s" % (self.first_name, self.last_name))

        width = 250
        height = 250
        size = (width, height)
        is_same = False
        if self.image:
            try:
                this = Student.objects.get(id=self.id)
                if this.image == self.image:
                    is_same = True
            except:
                pass  # when new image then we do nothing, normal case

            image = Img.open(StringIO.StringIO(self.image.read()))
            (imw, imh) = image.size
            if (imw > width) or (imh > height):
                image.thumbnail(size, Img.ANTIALIAS)

            # If RGBA, convert transparency
            if image.mode == "RGBA":
                image.load()
                background = Img.new("RGB", image.size, (255, 255, 255))
                background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
                image = background

            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=60)
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
                                              'image/jpeg', output.len, None)

        try:
            this = Student.objects.get(id=self.id)
            if this.image == self.image or is_same:
                self.image = this.image
            else:
                this.image.delete(save=False)
        except:
            pass  # when new image then we do nothing, normal case

        super(Student, self).save(*args, **kwargs)

    def send_activation_email(self):
        subject = "Thank you for registering at Leapkit.com"

        email = "Hi %s \n\n " \
                "Welcome to the Leapkit.com! \n" \
                " We are happy to have you on board! \n" \
                "We really hope that you can use the platform and take your school projects to the next level! \n" \
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


class StudentProjectManager(models.Manager):
    def get_own_projects(self, user):
        projects = super(StudentProjectManager, self).get_queryset().filter(is_active=True, project_owner=user)
        return projects

    def get_published_queryset(self):
        projects = super(StudentProjectManager, self).get_queryset().filter(is_active=True, published=True)
        return projects

    def get_own_published_queryset(self, user):
        projects = super(StudentProjectManager, self).get_queryset().filter(is_active=True, published=True, project_owner=user)
        return projects

    def get_own_drafts_queryset(self, user):
        projects = super(StudentProjectManager, self).get_queryset().filter(is_active=True, published=False,
                                                                            project_owner=user)
        return projects

class StudentProject(Project):
    """
    This model is to be used for all projects created by companies.
    It contains all the fields needed to create an advanced company project.
    """

    project_owner = models.ForeignKey(Student)
    objects = StudentProjectManager()

class LinkedInProfile(models.Model):

    """
    This model is used to represent a students LinkedIn information.
    """
    # The userid/link to a specific user
    leapkituser = models.OneToOneField(User)

    # Last time the data was modified/updated.
    modified = models.DateTimeField(auto_now_add=True)

    # Profile ID from linkedIn.
    linkedin_id = models.IntegerField()

    # Name information from LinkedIn
    firstName =  models.TextField()
    maidenName = models.TextField()
    lastName = models.TextField()

    # Misc information from LinkedIn
    location = models.TextField()
    specialities = models.TextField()
    positions = models.TextField()
    pictureUrl = models.TextField()
    publicProfileUrl = models.TextField()

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        :return: First name + last name, with a space in between
        """
        return "%s %s" % (self.firstName, self.lastName)

class Language(models.Model):
   lang_id = models.IntegerField()
   name = models.CharField(max_length = 30)
   level = models.CharField(max_length = 30)
   profile = models.ForeignKey(LinkedInProfile)

class Course(models.Model):
   course_id  = models.IntegerField()
   name = models.CharField(max_length = 81)
   profile = models.ForeignKey(LinkedInProfile)

class Skill(models.Model):
   skill_id = models.IntegerField()
   name = models.CharField(max_length = 81)
   profile = models.ForeignKey(LinkedInProfile)

class Education(models.Model):
   edu_id = models.IntegerField()
   schoolName = models.CharField(max_length=100)
   fieldOfStudy = models.CharField(max_length=100)
   degree = models.CharField(max_length=100)
   profile = models.ForeignKey(LinkedInProfile)

def insertLinkedInProfile(p, User):
    profile = LinkedInProfile(leapkituser = User,
                              linkedin_id = int(p.id),
                              firstname = p.firstName,
                              maidenName = p.maidenName,
                              lastName = p.lastName,
                              headline = p.headline,
                              location = p.location,
                              industry = p.industry,
                              summary = p.summary,
                              specialities = p.specialities,
                              positions = p.positions,
                              pictureUrl = p.pictureUrl,
                              publicProfileUrl = p.publicProfileUrl,
                              formattedName = p.formattedName,
                              phoneticFirstName = p.phoneticFirstName,
                              phoneticLastName = p.phoneticLastName,
                              formattedPhoneticName = p.formattedPhoneticName)
    profile.save()

    for s in p.skills:
        ski = Skill(skill_id = int(s.id), name = s.name, profile = profile)
        ski.save()

    for l in p.languages:
        lang = Language(lang_id = int(l.id), name = l.name, level = l.Level,
                profile = profile)
        lang.save()

    for e in p.educations:
        edu = Education(edu_id = int(e.id), schoolname = e.schoolName,
                fieldOfStudy = e.fieldOfStudy, degree = e.degree,
                profile = profile)
        edu.save()

    for c in p.courses:
        cou = Course(course_id = int(c.id), name = c.name, profile = profile)
        c.save()
