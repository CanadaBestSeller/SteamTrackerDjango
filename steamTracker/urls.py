from django.conf.urls import patterns, url

from steamTracker import views

urlpatterns = patterns(
    '',
    url(r'^$', views.test, name='test'),
    # url(r'^(?P<question_id>\d+)/vote$', views.vote, name='vote'),
)
