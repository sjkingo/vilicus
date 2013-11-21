from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^dashboard/$', 'manager.views.dashboard', name='dashboard'),
)
