from django.contrib import admin

from models import Student, StudentProject, LinkedInProfile, Skill

class LinkedInProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['leapkituser',
                           'linkedin_id',
                           'firstName',
                           'lastName',
                           'specialities',
                           'positions',
                           'pictureUrl',
                           'publicProfileUrl'
                           ]}),
    ]

    readonly_fields = ('modified',)
    list_display = ('leapkituser', 'firstName', 'lastName', 'modified')
    search_fields = ['leapkituser', 'firstName']
    list_filter = ['specialities']


admin.site.register(LinkedInProfile, LinkedInProfileAdmin)

class SkillAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields' : ['skill_id', 'name', 'profile']}),]
  list_display = ('skill_id', 'name', 'profile')
  search_fields = ['name','profile']

admin.site.register(Skill, SkillAdmin)


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user',
                           'first_name',
                           'last_name',
                           'image',
                           'date_of_birth',
                           'gender',
                           'education_level',
                           'country',
                           'institution',
                           'line_of_study',
                           'description',
                           'cv'
                           ]}),
    ]

    list_display = ('first_name', 'last_name', 'institution', 'times_logged_in')
    search_fields = ['institution', 'first_name']
    list_filter = ['institution', 'gender', 'times_logged_in']


admin.site.register(Student, StudentAdmin)


class StudentProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project_owner',
                           'title',
                           'contact_person',
                           'contact_email',
                           'contact_phone',
                           'start_date',
                           'end_date',
                           'students_needed',
                           'short_description',
                           'full_description',
                           'project_document',
                           'published',
                           'project_type',
                           'education_requirements',
                           'country_requirements',
                           'university_requirements',
                           'related_lines_of_study',
                           'job_functions',
                           'open_for_applications',
                           'is_active',
                           'views',
                           'detail_views']}),
    ]

    list_display = ('project_owner', 'title', 'contact_person', 'contact_email', )
    search_fields = ['project_owner', 'title']
    list_filter = ['contact_person', 'open_for_applications', 'published', 'is_active', ]


admin.site.register(StudentProject, StudentProjectAdmin)
