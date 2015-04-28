from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from manager.api.resources import v1_api

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^', include('dashboard.urls')),
]
