import debug_toolbar
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r"^", include("search_engine.urls")),
    path("admin", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True)), name="graphql"),
]
