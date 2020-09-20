import debug_toolbar
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView

urlpatterns = [
    path("simple", include("search_engine.urls")),
    path("admin", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True)), name="graphql"),
    re_path(".*", TemplateView.as_view(template_name="index.html")),
]
