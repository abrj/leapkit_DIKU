from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

import root.views as views

admin.autodiscover()

urlpatterns = patterns('',
                       # URLs used when not signed in (views and functionality stored in root app).
                       # They are accessed here, to make the URL prettier

                       # Basic navigation urls
                       url(r'^$', views.HomepageView.as_view(), name='home'),
                       url(r'', include('social_auth.urls', namespace='social')),
                       url(r'^pricing/$', views.ProjectPricingView.as_view(), name='project_pricing'),
                       url(r'^about-leapkit/$', views.AboutLeapkitView.as_view(), name='about_leapkit'),
                       url(r'^FAQ/$', views.FAQView.as_view(), name='FAQ'),
                       url(r'^terms-of-usage/$', views.TermsOfUsageView.as_view(), name='terms_of_usage'),
                       # All urls related to contacting leapkit
                       url(r'^contact-leapkit/$', views.ContactLeapkitView.as_view(), name='contact_leapkit'),
                       url(r'^contact-leapkit/success/$', views.contact_success_redirect, name='contact_success'),

                       # All other URLs are stored in their respective app.
                       url(r'^students/', include('students.urls', namespace="students")),
                       url(r'^companies/', include('companies.urls', namespace="companies")),


                       #url('', include('students.urls', namespace="test")),

                       url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'root.views.PageNotFoundView'
handler500 = 'root.views.ErrorView'
handler403 = 'root.views.PermissionDeniedView'
handler400 = 'root.views.BadRequestView'