from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include("search_engine.urls")),
    url(r'^admin/', include(admin.site.urls)),
]
