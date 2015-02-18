from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^sign-up/$', views.CompanySignUpView.as_view(), name='sign_up'),
    url(r'^sign-up/(?P<slug>[a-z0-9-]+)/company-sign-up-success/$', views.company_sign_up_success_view, name='sign_up_success'),
    url(r'^login/$', views.CompanyLogInView.as_view(), name='log_in'),
    url(r'^login-check/$', views.login_check, name='log_in_check'),
    url(r'^log-out/$', views.sign_out_view, name='log_out'),
    url(r'^change_password/(?P<pk>\d+)/$', views.ChangePasswordView.as_view(), name='change_password'),
    url(r'^handbook/$', views.HandBookView.as_view(), name='handbook'),
    url(r'^terms-of-usage/$', views.CompanyTermsOfUsage.as_view(), name="company_terms_of_usage"),
    url(r'^frequently-asked-questions/$', views.CompanyFAQView.as_view(), name='company_FAQ'),
    url(r'^feedback/$', views.CompanyFeedback.as_view(), name="company_feedback"),
    url(r'^projects/create-new-project/$', views.CompanyProjectCreationView.as_view(), name='create_project'),
    url(r'^projects/$', views.CompanyProjectListView.as_view(), name='list_projects'),
    url(r'^projects/delete/(?P<slug>[a-z0-9-]+)$', views.company_project_delete_view, name='delete_project'),
    url(r'^projects/alter-contact/(?P<slug>[a-z0-9-]+)$', views.company_project_alter_contact_view, name='alter_contact_option'),
    url(r'^projects/details/(?P<slug>[a-z0-9-]+)$', views.CompanyProjectDetailView.as_view(), name='project_details'),
    url(r'^projects/update/(?P<slug>[a-z0-9-]+)$', views.CompanyProjectUpdateView.as_view(), name='update_project'),
    url(r'^projects/pricing/(?P<slug>[a-z0-9-]+)/$', views.ProjectPricingView.as_view(), name='project_pricing'),
    url(r'^profile/update/(?P<slug>[a-z0-9-]+)$', views.UpdateCompanyView.as_view(), name='update_profile'),
    url(r'^profile/(?P<slug>[a-z0-9-]+)/$', views.CompanyView.as_view(), name='profile'),
)