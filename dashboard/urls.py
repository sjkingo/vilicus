from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^dashboard/$', 'dashboard.views.dashboard', name='dashboard'),
)
