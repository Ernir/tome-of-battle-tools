from django.conf.urls import patterns, url
from search_engine import views

urlpatterns = \
    patterns('',
             url(r"^$", views.index, name="index"),
             url(r"^search/$", views.search, name="search"),
             url(r"maneuvers/(?P<man_slug>.+)/", views.maneuver, name="maneuver"),
             url(r"about/", views.about, name="about"),
             url(r"maneuvers-alphabetical/", views.maneuvers_alphabetical, name="maneuvers_alphabetical"),
             url(r"maneuvers-by-discipline/", views.maneuvers_by_discipline, name="maneuvers_by_discipline"),
             url(r"maneuvers-by-level/", views.maneuvers_by_level, name="maneuvers-by-level"),

             url(r"^api/search/$", views.perform_search, name="perform_search"),
    )