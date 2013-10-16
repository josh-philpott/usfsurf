from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usfsurf.views.home', name='home'),
    # url(r'^usfsurf/', include('usfsurf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls), {}, 'admin_url_name'),
	url(r'^events/', include('events.urls') ),
    url(r'^about/', TemplateView.as_view(template_name = 'about.html'), {}, 'contact_url_name'),
	url(r'^contact/', TemplateView.as_view(template_name = 'contact.html'), {}, 'contact_url_name'),
	url(r'^home/', TemplateView.as_view(template_name = 'home.html'), {}, 'home_url_name'),
    url(r'^$', TemplateView.as_view(template_name = 'home.html')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),


)

urlpatterns += staticfiles_urlpatterns()
