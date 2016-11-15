from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    'documentation.views',

    url(r'^$', 'documentation', 'index.html'),
    url(r'^(?P<path>.*)$', 'documentation', name="path"),
]
