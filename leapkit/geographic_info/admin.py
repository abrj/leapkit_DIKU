from django.contrib import admin

from .models import Country, Region, City, ZipCode


"""
Below is the admin section for the geographical models
"""


class CountryAdmin(admin.ModelAdmin):
    fieldsets = (None, {'fields': ['name', 'country_code']}),

    list_display = ('name', 'country_code')
    search_fields = ['name']


admin.site.register(Country, CountryAdmin)


class RegionAdmin(admin.ModelAdmin):
    fieldsets = (None, {'fields': ['name', 'area_code', 'country']}),

    list_display = ('name', 'country', 'area_code', )
    search_fields = ['name']


admin.site.register(Region, RegionAdmin)


class CityAdmin(admin.ModelAdmin):
    fieldsets = (None, {'fields': ['name', 'region']}),

    list_display = ('name', 'region',)
    search_fields = ['name']


admin.site.register(City, CityAdmin)


class ZipCodeAdmin(admin.ModelAdmin):
    fieldsets = (None, {'fields': ['zip_code', 'city']}),

    list_display = ('zip_code', 'city',)
    search_fields = ['zip_code']


admin.site.register(ZipCode, ZipCodeAdmin)

"""
Below is the admin section for the professional meta models
"""






