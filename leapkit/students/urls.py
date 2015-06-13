from django.conf.urls import patterns, url

from django.views.generic.base import RedirectView

from django.http import HttpResponseRedirect



from . import views


urlpatterns = patterns('',
                       # URLs used when not signed in (views and functionality stored in root app).
                       # They are accessed here, to make the URL prettier
                       url(r'^sign-up/$', views.StudentSignUpView.as_view(), name='sign_up'),
                       url(r'^sign-up/(?P<slug>[a-z0-9-]+)/student-sign-up-success/$', views.student_sign_up_success, name='sign_up_success'),
                       url(r'^login/$', views.StudentLogInView.as_view(), name='log_in'),
                       url(r'^login-check/$', views.login_check, name='log_in_check'),
                       url(r'^log-out/$', views.sign_out_view, name='log_out'),
                       url(r'^feedback/$', views.StudentFeedBack.as_view(), name="student_feedback"),
                       url(r'^terms-of-usage/$',
                           views.StudentTermsOfUsage.as_view(),
                           name="students_terms_of_usage"),
                       url(r'^change_password/(?P<pk>\d+)/$', views.ChangePasswordView.as_view(),
                           name='change_password'),
                       url(r'^frequently-asked-questions/$', views.StudentFAQView.as_view(), name='students_FAQ'),
                       url(r'^projects/create-new-project/$', views.StudentProjectCreationView.as_view(),
                           name='create_student_project'),
                       url(r'^projects/$', views.ListAllProjectsView.as_view(), name='all_projects'),
                       url(r'^projects/filter/$', views.all_projects_filter, name='all_projects_filtered'),
                       url(r'^projects/page/(?P<page>\d+)/$', views.ListAllProjectsView.as_view(),
                           name='all_projects_paginated'),
                       url(r'^projects/detail/(?P<slug>[a-z0-9-]+)/$', views.AllProjectDetailView.as_view(),
                           name='all_projects_detail'),
                       url(r'^projects/send-email/(?P<slug>[a-z0-9-]+)$',
                           views.SendMailView.as_view(),
                           name='send_email'),
                       url(r'^own-projects/$', views.StudentOwnProjectListView.as_view(), name='own_student_projects'),
                       url(r'^own-projects/delete/(?P<slug>[a-z0-9-]+)$', views.student_project_delete_view,
                           name='delete_student_project'),
                       url(r'^own-projects/alter-contact/(?P<slug>[a-z0-9-]+)$',
                           views.student_project_alter_contact_view,
                           name='alter_contact_option'),
                       url(r'^own-projects/details/(?P<slug>[a-z0-9-]+)$', views.StudentProjectDetailView.as_view(),
                           name='student_project_details'),
                       url(r'^own-projects/update/(?P<slug>[a-z0-9-]+)$', views.StudentProjectUpdateView.as_view(),
                           name='update_student_project'),
                       url(r'^profile/update/(?P<slug>[a-z0-9-]+)/$', views.UpdateStudentProfileView.as_view(),
                           name='update_student_profile'),
                       url(r'^profile/(?P<slug>[a-z0-9-]+)/$', views.StudentView.as_view(), name='profile'),
                       #url('www.google.com', views.test, name='test'),
                       #url('', RedirectView.as_view(url='www.google.com', permanent=False), name='test'),
                       #url(r'^$', views.test, name='test'),

                       #url(r'^test/$', views.test, name='test'), #works
                       url(r'red', views.linkedin_redirect, name='linkedin_redirect'), #works
                       #url(r'^profile/(?P<slug>[a-z0-9-]+)/$', views.test, name='test'),
                       url(r'stage', views.stage, name='stage'), #works
                       url(r'demo', views.demo, name='demo'),
)
