from django.conf.urls import patterns, include, url
from home import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^steam_tracker/', include('steamTracker.urls', namespace='steamTracker')),
)
