from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='events_url_name')
)
