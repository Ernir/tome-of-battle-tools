from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    (r'^', include("search_engine.urls")),
    (r'^admin/', include(admin.site.urls)),
)