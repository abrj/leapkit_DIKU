# Register your models here.
from django.contrib import admin

from models import Project, JobFunction


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title',
                           'slug',
                           'views',
                           'detail_views',
                           'contact_person',
                           'is_active']}),
    ]

    list_display = ('title', 'is_active')
    search_fields = ['title', 'contact_email']
    list_filter = ['is_active', 'published' ]


admin.site.register(Project, ProjectAdmin)


class JobFunctionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]

    list_display = ('name', )

admin.site.register(JobFunction, JobFunctionAdmin)