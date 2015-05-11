from calendar import monthrange
from datetime import timedelta
import uuid
import StringIO

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as Img
import os


def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('Institutions/logos/', filename)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    number_of_students = models.IntegerField(default=0)
    logo = models.ImageField(upload_to=get_image_path,
                             blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return "%s  -  %s" % (self.short_name, self.name)

    def add_one_student(self):
        self.number_of_students += 1
        self.save()

    def save(self, *args, **kwargs):
        width = 250
        height = 250
        size = (width, height)
        is_same = False
        if self.logo:
            try:
                this = Institution.objects.get(id=self.id)
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
            this = Institution.objects.get(id=self.id)
            if this.logo == self.logo or is_same:
                self.logo = this.logo
            else:
                this.logo.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case

        super(Institution, self).save(*args, **kwargs)

    class Meta:
        ordering = ('short_name', "name", )
        verbose_name = _('institution')
        verbose_name_plural = _('institutions')


class Department(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(Institution)
    website = models.URLField(blank=True)
    address = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.university.short_name)

    class Meta:
        ordering = ("name", )


class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department)
    start_date = models.DateField()
    end_date = models.DateField()
    ects_points = models.FloatField()
    professor = models.ForeignKey(Professor)
    language = models.CharField(max_length=20, blank=True)
    learning_goals = models.TextField(blank=True)
    description = models.TextField(blank=True)
    learning_activities = models.TextField(blank=True)
    obligatory_activities = models.TextField(blank=True)
    evaluation_form = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("department", "name", )

    def get_course_length(self):
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


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', ]
        verbose_name = "Field of Study"
        verbose_name_plural = "Fields of Study"

class Skill(models.Model):
    name = models.CharField(max_length = 81)
    fieldOfStudy = models.ForeignKey(FieldOfStudy)

    def __unicode__(self):
        return self.get_skill()

    def get_skill(self):
        return "%s" % (self.name)


