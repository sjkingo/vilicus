from django.contrib import admin

from manager.models import *

class AgentAdmin(admin.ModelAdmin):
    readonly_fields = ('last_checkin', 'version', 'guid')

admin.site.register(Agent, AgentAdmin)

admin.site.register(WindowsService)

class WindowsServiceLogAdmin(admin.ModelAdmin):
    readonly_fields = ('service', 'timestamp', 'actual_status', 'action_taken')

admin.site.register(WindowsServiceLog, WindowsServiceLogAdmin)

class PerformanceLogEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('agent', 'timestamp', 'cpu_usage')
admin.site.register(PerformanceLogEntry, PerformanceLogEntryAdmin)
