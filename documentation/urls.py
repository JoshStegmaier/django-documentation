from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from .views import documentation

urlpatterns = [
    url(r'^$', documentation, 'index.html'),
    url(r'^(?P<path>.*)$', documentation, name="path"),
]
