from django.contrib import admin

from queries.models import FAQuestion, UserQuestion, CompanyEmailContact


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question', 'answer', 'subject']}),
    ]

    list_display = ('question', 'answer', 'subject')
    search_fields = ['question']
    list_filter = ['subject']


admin.site.register(FAQuestion, QuestionAdmin)


class UserQueryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'email', 'body', 'has_been_answered', 'answer']}),
    ]

    list_display = ('name', 'email', 'has_been_answered')
    list_filter = ['has_been_answered', 'created']


admin.site.register(UserQuestion, UserQueryAdmin)


class CompanyEmailContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject', 'sender', 'receiver', 'contact_email',  'body']}),
    ]

    list_display = ('sender', 'receiver', 'subject')
    list_filter = ['sender', 'receiver']


admin.site.register(CompanyEmailContact, CompanyEmailContactAdmin)