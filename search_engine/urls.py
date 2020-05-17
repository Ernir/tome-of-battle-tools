from django.conf.urls import url
from search_engine import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^search/$", views.search, name="search"),
    url(r"^maneuvers/(?P<man_slug>.+)/", views.maneuver, name="maneuver"),
    url(r"^about/", views.about, name="about"),
    url(
        r"^maneuvers-alphabetical/",
        views.maneuvers_alphabetical,
        name="maneuvers_alphabetical",
    ),
    url(
        r"^maneuvers-by-discipline/",
        views.maneuvers_by_discipline,
        name="maneuvers_by_discipline",
    ),
    url(r"^maneuvers-by-level/", views.maneuvers_by_level, name="maneuvers_by_level"),
    url(r"^statistics/", views.statistics, name="statistics"),
    url(r"^simple-search/", views.simple_search, name="simple_search"),
    url(r"^api/search/$", views.perform_search, name="perform_search"),
    url(r"^api/get-all-maneuvers/$", views.get_maneuvers, name="get_maneuvers"),
    url(r"^api/statistics/errata/$", views.errata_numbers, name="errata_numbers"),
    url(r"^api/statistics/types/$", views.type_numbers, name="type_numbers"),
    url(
        r"^api/statistics/disciplines/$",
        views.discipline_numbers,
        name="discipline_numbers",
    ),
]
