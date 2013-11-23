from tastypie import fields
from tastypie.api import Api
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.serializers import Serializer

from manager.models import *

v1_api = Api(api_name='v1')

class AgentResource(ModelResource):
    class Meta:
        queryset = Agent.objects.all()
        filtering = {
            'id': ALL,
        }

        allowed_methods = ['get', 'put']
        authorization = Authorization()
        serializer = Serializer()

v1_api.register(AgentResource())

class WindowsServiceResource(ModelResource):
    agent = fields.ForeignKey(AgentResource, 'agent')

    class Meta:
        queryset = WindowsService.objects.all()
        filtering = {
            'agent': ALL_WITH_RELATIONS,
        }

        allowed_methods = ['get']
        authorization = Authorization()
        serializer = Serializer()

v1_api.register(WindowsServiceResource())

class WindowsServiceLogResource(ModelResource):
    service = fields.ForeignKey(WindowsServiceResource, 'service')

    class Meta:
        queryset = WindowsServiceLog.objects.all()
        filtering = {
            'service': ALL_WITH_RELATIONS,
        }

        allowed_methods = ['get', 'post']
        authorization = Authorization()
        serializer = Serializer()

v1_api.register(WindowsServiceLogResource())

class PerformanceLogEntryResource(ModelResource):
    agent = fields.ForeignKey(AgentResource, 'agent')

    class Meta:
        queryset = PerformanceLogEntry.objects.all()
        filtering = {
            'agent': ALL_WITH_RELATIONS,
        }

        allowed_methods = ['post']
        authorization = Authorization()
        serializer = Serializer()

v1_api.register(PerformanceLogEntryResource())
