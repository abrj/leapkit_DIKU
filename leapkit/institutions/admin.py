from django.contrib import admin

# Register your models here.
from models import (Institution, Course, Department, Professor, FieldOfStudy)


class InstitutionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name',
                           'short_name',
                           'address',
                           'number_of_students',
                           'website',
                           'logo'
        ]}),
    ]

    list_display = ('short_name', 'name', 'number_of_students')
    search_fields = ['short_name', 'name']
    list_filter = ['name']


admin.site.register(Institution, InstitutionAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name',
                           'university',
                           'website'
        ]}),
    ]

    list_display = ('name', 'university')
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Department, DepartmentAdmin)


class ProfessorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name',
                           'email',
                           'website'
        ]}),
    ]

    list_display = ('name', 'email')
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Professor, ProfessorAdmin)


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name',
                           'department',
                           'start_date',
                           'end_date',
                           'ects_points',
                           'professor',
                           'language',
                           'learning_goals',
                           'description',
                           'learning_activities',
                           'obligatory_activities',
                           'evaluation_form'
        ]}),
    ]

    list_display = ('name', 'department')
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Course, CourseAdmin)


class LineOfStudyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]

    list_display = ('name', )
    search_fields = ['name']


admin.site.register(FieldOfStudy, LineOfStudyAdmin)


