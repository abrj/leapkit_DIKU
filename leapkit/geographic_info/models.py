from django.db import models

# Create your models here.

"""
The next section contains all the models used to control and store the geographical information
"""


class Country(models.Model):
    name = models.CharField(max_length=254)
    country_code = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("name", )
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Region(models.Model):
    name = models.CharField(max_length=254)
    country = models.ForeignKey(Country)
    area_code = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("country", "name", )


class City(models.Model):
    name = models.CharField(max_length=254)
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("region", "name", )
        verbose_name = "City"
        verbose_name_plural = "Cities"


class ZipCode(models.Model):
    zip_code = models.CharField(max_length=100)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return "%s - %s" % (self.zip_code, self.city.name)

    class Meta:
        ordering = ("zip_code", )
        verbose_name = "Zip Code"
        verbose_name_plural = "Zip Codes"


class Street(models.Model):
    name = models.CharField(max_length=254)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.city.name)

    class Meta:
        ordering = ("city", "name")

"""
The next section contains all the models used to control and store the professional information for students, companies
and universities.
"""





