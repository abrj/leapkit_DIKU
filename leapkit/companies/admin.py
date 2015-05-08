from django.contrib import admin

from .models import Company, CompanyProject, Industry, ProjectPackage


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name',
                           'logo',
                           'address',
                           'industry',
                           'company_size',
                           'year_founded',
                           'about',
                           'overview',
                           'mission',
                           'website',
                           'projects_available',
                           'region',
                           'country',



        ]}),
    ]

    list_display = ('user', 'name', 'industry', 'times_logged_in')
    search_fields = ['name', 'address']
    list_filter = ['industry', 'date_joined', 'projects_available', 'times_logged_in']


admin.site.register(Company, CompanyAdmin)


class CompanyProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            # Basic Information
            'project_owner',
            'title',
            'contact_person',
            'contact_email',
            'contact_phone',
            'start_date',
            'end_date',
            'students_needed',
            'web_page',
            'project_type',



            # Project information
            'short_description',
            'full_description',

            'project_document',

            # Requirements
            'education_requirements',
            'university_requirements',
            'job_functions',

            # Other Info
            'payment',
            'nda_required',
            'involvement',
            'related_lines_of_study',
            'thesis_or_internship_required',
            'resume_required',
            'published',
            'is_active',
            'views',
            'detail_views'
        ]}),
    ]

    list_display = ('project_owner', 'title', 'contact_person', 'contact_email', 'views', 'detail_views', )
    search_fields = ['project_owner', 'title']
    list_filter = ['contact_person', 'open_for_applications', 'published', 'is_active', ]


admin.site.register(CompanyProject, CompanyProjectAdmin)


class IndustryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]

    list_display = ('name', )
    search_fields = ['name']


admin.site.register(Industry, IndustryAdmin)


class ProjectPackageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['company_name',
                           'email',
                           'invoice_sent',
                           'payment_received',
                           'type',
                           'note']}),
    ]

    list_display = ('company_name', 'email', 'buying_date', 'type', 'invoice_sent', 'payment_received')
    search_fields = ['company_name', 'email']
    list_filter = ['buying_date', 'invoice_sent', 'payment_received', 'type']


admin.site.register(ProjectPackage, ProjectPackageAdmin)