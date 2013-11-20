from django.shortcuts import render

from manager.models import *

def dashboard(request, template='dashboard.html'):
    agents = Agent.objects.all()
    context = {'agents': agents}
    return render(request, template, context)
