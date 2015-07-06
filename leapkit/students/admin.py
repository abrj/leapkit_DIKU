from django.contrib import admin

from models import (Student, StudentProject, LinkedInProfile, Skill, Language,
    Course, Education,Position)

# class LinkedInProfileAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['leapkituser',
#                            'linkedin_id',
#                            'firstName',
#                            'lastName',
# #                          'positions',
# #                          'pictureUrl',
# #                          'publicProfileUrl'
#                            ]}),
#     ]
#
#     readonly_fields = ('modified',)
#     list_display = ('leapkituser', 'firstName', 'lastName', 'modified')
#     search_fields = ['leapkituser', 'firstName']
#
#
# admin.site.register(LinkedInProfile, LinkedInProfileAdmin)

class SkillAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields' : ['name', 'profile']}),]
  list_display = ('name', 'profile')
  search_fields = ['name','profile']

admin.site.register(Skill, SkillAdmin)
#
# class LanguageAdmin(admin.ModelAdmin):
#   fieldsets = [(None, {'fields' : ['name', 'level','profile']}),]
#   list_display = ('name', 'level', 'profile')
#   search_fields = ['name','level','profile']
#
# admin.site.register(Language, LanguageAdmin)
#
# class EducationAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields' : ['schoolName', 'fieldOfStudy',
#         'degree', 'profile']}),]
#     list_display = ('schoolName', 'fieldOfStudy', 'degree', 'profile')
#     search_fields = ['fieldOfStudy', 'degree', 'profile']
#
# admin.site.register(Education, EducationAdmin)
#
# class CourseAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields' : ['name', 'profile']}),]
#     list_display = ('name', 'profile')
#     search_fields = ['name', 'profile']
#
# admin.site.register(Course, CourseAdmin)
#
# class PositionAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields' : ['jobtitle', 'company', 'isCurrent',
#         'profile']}),]
#     list_display = ('jobtitle', 'profile')
#     search_fields = ['jobtitle', 'company', 'isCurrent', 'profile']
#
# admin.site.register(Position, PositionAdmin)


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
                           'cv',
                           'linkedin_url'
                           ]}),
    ]

    list_display = ('first_name', 'last_name', 'institution', 'times_logged_in','linkedin_url')
    search_fields = ['institution', 'first_name']
    list_filter = ['institution', 'gender', 'times_logged_in','linkedin_url']


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
