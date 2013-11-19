from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from manager.api.resources import *
v1_api = Api(api_name='v1')
v1_api.register(AgentResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vilicus.views.home', name='home'),
    # url(r'^vilicus/', include('vilicus.foo.urls')),

    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
