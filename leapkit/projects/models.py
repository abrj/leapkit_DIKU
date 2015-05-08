# coding=utf-8
from calendar import monthrange
from datetime import timedelta
import os
from django.template.defaultfilters import slugify
from django.db import models
from pip import autocomplete
import re
from geographic_info.models import Country, Region
from institutions.models import Course, Institution, FieldOfStudy



class JobFunction(models.Model):
    name = models.CharField(max_length=254)

    def __unicode__(self):
        return self.name


class ProjectManager(models.Manager):

    def get_published_queryset(self):
        projects = super(ProjectManager, self).get_queryset().filter(is_active=True, published=True)
        return projects


class Project(models.Model):
    """
    This model is to be used for all projects
    It contains all the fields needed to create the base of a project.
    """

    title = models.CharField(max_length=254,
                             help_text="Provide a title for your project.",
                             verbose_name="Project Title")
    contact_person = models.CharField(max_length=254,
                                      help_text="Provide a name for the person in charge of the project.")
    contact_email = models.EmailField(max_length=254,
                                      help_text="Provide an email for the person in charge of the project.")
    contact_phone = models.CharField(max_length=12,
                                     verbose_name="Contact Telephone",
                                     blank=True,
                                     help_text="Here you can provide a telephone number "
                                               "for the person in charge of the project.")

    start_date = models.DateField(help_text="Please select the latest date a student can join the project.",
                                  null=True,
                                  blank=True)
    end_date = models.DateField(help_text="Please select when the project is finished.",
                                null=True,
                                blank=True)

    students_needed = models.IntegerField(help_text="Please select how many students that are needed for this project.",
                                          blank=True,
                                          null=True)
    full_description = models.TextField(help_text="Please provide a description of the project. In this section, "
                                                  "the students are especially interested in the subject area and "
                                                  "goal of the project, including any milestones.")
    short_description = models.TextField(max_length=250,
                                         help_text="Please provide a short description. This is used "
                                                   "to give a brief introduction of the project when it is listed.")

    project_document = models.FileField(upload_to='projects/files/',
                                        blank=True,
                                        help_text="Here you can provide a relevant file "
                                                  "for the project.")

    published = models.BooleanField(default=False, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    views = models.IntegerField(blank=True, default=0)
    detail_views = models.IntegerField(blank=True, default=0)


    # Other information
    BACHELOR = "BSC"
    MASTER = "MSC"
    ALL = "ALL"

    STUDENT_TYPE = {
        (BACHELOR, "Bachelor Students"),
        (MASTER, "Master Students"),
        (ALL, "All students")
    }

    education_requirements = models.CharField(max_length=3,
                                              choices=STUDENT_TYPE,
                                              default=ALL,
                                              help_text="Please select if the project is suitable "
                                                        "for bachelor, masters or All. ",
                                              verbose_name="Education Preferences")


    # Many to many fields, used to keep track of the meta data
    country_requirements = models.ManyToManyField(Country,
                                                  null=True,
                                                  blank=True,
                                                  help_text="Please select if your project is only relevant "
                                                            "for students in particular countries.",
                                                  verbose_name="Country Preferences"
    )
    region_requirements = models.ManyToManyField(Region,
                                                 null=True,
                                                 blank=True,
                                                 help_text="Please select if your project is only "
                                                           "relevant for students in particular geographical regions.",
                                                 verbose_name="Region Preferences"
    )

    course_requirements = models.ManyToManyField(Course,
                                                 null=True,
                                                 blank=True,
                                                 help_text="We have hand-picked a range of project-oriented courses"
                                                           " with high freedom for the students to pick their own"
                                                           " projects. A brief description of the course can be found "
                                                           "in our partnership course database (opens in new tab). If"
                                                           " you select any of the courses from the list below, "
                                                           "we will directly inform student users from "
                                                           "those courses that your project is available.",
                                                 verbose_name="Course Preferences"
    )
    university_requirements = models.ManyToManyField(Institution,
                                                     null=True,
                                                     blank=True,
                                                     help_text="Please select if this project is only relevant for"
                                                               " students from a particular university.",
                                                     verbose_name="University Preferences"
    )
    related_lines_of_study = models.ManyToManyField(FieldOfStudy,
                                                    null=True,
                                                    blank=True,
                                                    related_name="Related Lines of Study",
                                                    help_text="You have the option to attach tags to your project. "
                                                              "Tags are keywords that students can search for to "
                                                              "find projects connected to those specific concepts. "
                                                              "They can be any word related to your project.")

    job_functions = models.ManyToManyField(JobFunction,
                                           null=True,
                                           blank=True,
                                           related_name="Related job functions",
                                           help_text="Please choose which job functions students will work with in"
                                                     " relation to this project")

    open_for_applications = models.BooleanField(default=True)

    # Basic fields, used to keep track of the profile
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = ProjectManager()


    def __unicode__(self):
        return self.title

    def get_project_universities(self):
        return self.university_requirements


    def get_project_document_name(self):
        return os.path.basename(self.project_document.name)


    def get_project_length(self):
        if (self.end_date - self.start_date).days > 50:
            return "%i %s" % (self.month_delta(self.start_date, self.end_date), "Months")

        return "%i %s" % ((self.end_date - self.start_date).days, "Days")

    def month_delta(self, start_date, end_date):
        delta = 0
        while True:
            mdays = monthrange(start_date.year, start_date.month)[1]
            start_date += timedelta(days=mdays)
            if start_date <= end_date:
                delta += 1
            else:
                break
        return delta


    def save(self, *args, **kwargs):
        if not self.slug:
            self.unique_slugify(value=self.title)

        super(Project, self).save(*args, **kwargs)

    def _slug_strip(self, value, separator='-'):
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

#The -created makes lists of project be sorted by creation date in descending order
    class Meta:
        ordering = ['-created', 'start_date', 'title', ]