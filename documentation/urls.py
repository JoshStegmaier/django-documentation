from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from .views import documentation

urlpatterns = [
    url(r'^$', documentation, kwargs={'path' : 'index.html'}),
    url(r'^(?P<path>.*)$', documentation, name="path"),
]
