from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL
from tastypie.serializers import Serializer

from manager.models import *

class AgentResource(ModelResource):
    class Meta:
        queryset = Agent.objects.all()
        filtering = {
            'id': ALL,
        }

        allowed_methods = ['get', 'put']
        authorization = Authorization()
        serializer = Serializer()
