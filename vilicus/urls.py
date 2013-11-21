from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from manager.api.resources import v1_api

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    (r'^', include('dashboard.urls')),
)
