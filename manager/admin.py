from django.contrib import admin

from manager.models import *

class AgentAdmin(admin.ModelAdmin):
    readonly_fields = ('last_checkin', 'version', 'guid')

admin.site.register(Agent, AgentAdmin)

admin.site.register(Service)

class ServiceLogAdmin(admin.ModelAdmin):
    readonly_fields = ('service', 'timestamp', 'actual_status', 'action_taken')

admin.site.register(ServiceLog, ServiceLogAdmin)
