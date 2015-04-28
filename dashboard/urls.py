from django.conf.urls import url

urlpatterns = [
    url(r'^dashboard/$', 'dashboard.views.dashboard', name='dashboard'),
]
