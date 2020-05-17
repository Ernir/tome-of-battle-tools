import string

from django.conf import settings
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from search_engine.forms import SearchForm
from search_engine.models import Discipline, Maneuver, ManeuverType


def index(request):
    return render(request, "index.html")


def search(request):
    """
    Displays the main search page, to be later filled with data via AJAX.
    """
    return render(
        request, "search.html", {"form": SearchForm(), "debug": settings.DEBUG}
    )


def simple_search(request):
    """
    Displays a search page that works without JS.
    """

    # Maneuver list that will be displayed
    ml = Maneuver.objects
    # Maneuvers that have been errata'd should not be displayed.
    ml = ml.filter(has_errata_elsewhere=False)

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["maneuver_name"]:
                name = form.cleaned_data["maneuver_name"].strip()
                ml = ml.filter(name__icontains=name)
            if form.cleaned_data["level"]:
                ml = ml.filter(level__in=form.cleaned_data["level"])
            if form.cleaned_data["discipline"]:
                ml.select_related("discipline")
                ml = ml.filter(discipline__name__in=form.cleaned_data["discipline"])
            if form.cleaned_data["requirements"]:
                ml = ml.filter(requirements__in=form.cleaned_data["requirements"])
            if form.cleaned_data["type"]:
                ml.select_related("type")
                ml = ml.filter(type__name__in=form.cleaned_data["type"])
    else:
        form = SearchForm()

    return render(request, "simple_search.html", {"form": form, "results": ml})


def perform_search(request):
    """
    Generates a list of maneuvers to display based on POST parameters.
    Returns their names and slugs in JSON format.
    This is used by the "old" endpoint. Should not be called by the application itself as it is right now.
    """

    if request.method == "POST":
        post_body = request.POST

        # Maneuver list
        ml = Maneuver.objects
        # Maneuvers that have been errata'd should not be displayed.
        ml = ml.filter(has_errata_elsewhere=False)

        # Perform successive filtering based on POST contents.
        if len(post_body) > 0:
            if "maneuver_name" in post_body:
                name = post_body["maneuver_name"].strip()
                if len(name) > 0:
                    ml = ml.filter(name__icontains=name)

            if "level" in post_body:
                ml = ml.filter(level__in=post_body.getlist("level"))

            if "discipline" in post_body:
                ml = ml.filter(discipline__name__in=post_body.getlist("discipline"))

            if "requirements" in post_body:
                ml = ml.filter(requirements__in=post_body.getlist("requirements"))

            if "type" in post_body:
                ml = ml.filter(type__name__in=post_body.getlist("type"))

        return_list = []
        for mans in ml.values("name", "slug"):
            return_list.append({"name": mans["name"], "slug": mans["slug"]})
        return JsonResponse(return_list, safe=False)


def get_maneuvers(request):
    ml = Maneuver.objects.filter(has_errata_elsewhere=False).all()
    return_list = [m.serialize_to_dict() for m in ml]
    return JsonResponse(return_list, safe=False)


def maneuver(request, man_slug):
    """

    Defines the page of a single maneuver.
    Finds the maneuver based on its slugified name, passed in by man_slug.
    """
    the_maneuver = get_object_or_404(Maneuver, slug=man_slug)
    available_to = the_maneuver.discipline.initiator_classes.all()
    descriptors = the_maneuver.descriptor.all()

    return render(
        request,
        "maneuver.html",
        {
            "maneuver": the_maneuver,
            "initiator_classes": available_to,
            "descriptors": descriptors,
        },
    )


def maneuvers_alphabetical(request):
    """

    Defines an alphabetical index of maneuvers.
    Returns three "chunks" of maneuvers, each to be placed in a column.
    Each chunk is a dictionary with letters of the alphabet as keys,
    and lists of all maneuvers starting with each letter as their values.
    """
    alphabet = string.ascii_uppercase

    maneuver_bag = {}
    # The letters where we break the columns.
    # This could be calculated with a fancy algorithm, but that's overkill.
    chunk_breaks = ["F", "Q", "Z"]
    chunks = []

    mans = Maneuver.objects.filter(has_errata_elsewhere=False)
    for letter in alphabet:
        mans_starting_with_letter = mans.filter(name__startswith=letter).all()
        if len(mans_starting_with_letter) > 0:
            maneuver_bag[letter] = mans_starting_with_letter
        if letter in chunk_breaks:
            chunk_breaks.pop(0)
            chunks.append(maneuver_bag)
            maneuver_bag = {}

    return render(
        request,
        "maneuvers_alphabetical.html",
        {
            "maneuver_chunks": chunks,
            "title": "Alphabetical Maneuver Index",
            "alphabet": alphabet,
        },
    )


def maneuvers_by_discipline(request):
    """

    Defines a page containing a list of maneuvers indexed by their disciplines.
    """
    disciplines = Discipline.objects.all()

    return render(request, "maneuvers_by_discipline.html", {"disciplines": disciplines})


def maneuvers_by_level(request):
    """

    Defines a page containing an index similar to the one on pages 48 to 51 of the
    Tome of Battle.
    """

    levels = range(1, 10)
    disciplines = Discipline.objects.all()

    maneuvers = {}
    for level in levels:
        maneuvers_of_level = Maneuver.unique_objects.filter(level=level)
        sublist = {}
        for discipline in disciplines:
            sublist[discipline] = maneuvers_of_level.filter(discipline=discipline).all()
        maneuvers[level] = sublist

    return render(
        request,
        "maneuvers_by_level.html",
        {"maneuvers": maneuvers, "disciplines": disciplines},
    )


def statistics(request):
    """

    Calculates various interesting statistics to show.
    Don't go here on an empty DB, it will cause zero divisions.
    """

    # Reference to all maneuevers, excluding maneuvers made obsolete by unofficial errata.
    all_unique_num = Maneuver.unique_objects.count()

    # First item: Statistics on how many maneuvers have been modified by errata.
    errata_num = Maneuver.maneuvers_with_errata.count()
    errata_percent = round(errata_num / all_unique_num * 100)

    # Second item: Statistics on various types of maneuvers.
    type_overview = ManeuverType.get_type_overview()

    # Third item: Statistics on number of maneuvers per discipline.
    ordered_disciplines = Discipline.by_count().all()
    average_num = round(ordered_disciplines.aggregate(Avg("num_mans"))["num_mans__avg"])
    largest_discipline = ordered_disciplines[len(ordered_disciplines) - 1]
    largest_discipline_share = round(largest_discipline.num_mans / all_unique_num * 100)
    smallest_discipline = ordered_disciplines[0]
    smallest_discipline_share = round(
        smallest_discipline.num_mans / all_unique_num * 100
    )

    return render(
        request,
        "stats.html",
        {
            "number": all_unique_num,
            "errata_num": errata_num,
            "errata_percent": errata_percent,
            "types": type_overview,
            "average_num": average_num,
            "largest_discipline": largest_discipline,
            "largest_discipline_share": largest_discipline_share,
            "smallest_discipline": smallest_discipline,
            "smallest_discipline_share": smallest_discipline_share,
        },
    )


def errata_numbers(request):
    """
    Returns the number of maneuvers with and without errata, in JSON format.
    """

    all_num = Maneuver.objects.count()
    errata_num = Maneuver.maneuvers_with_errata.count()
    errata_free_num = all_num - errata_num * 2

    return_dict = {"errata_num": errata_num, "errata_free_num": errata_free_num}

    return JsonResponse(return_dict)


def type_numbers(request):
    """
    Returns the number of maneuvers of each maneuver type, in JSON format.
    """

    type_overview = ManeuverType.get_type_overview()

    return JsonResponse(type_overview)


def discipline_numbers(request):
    """
    Returns the number of maneuvers in each discipline, in JSON format.
    """

    disciplines = Discipline.by_count().all()

    discipline_overview = []
    for discipline in disciplines:
        discipline_overview.insert(
            0, ({"name": discipline.name, "count": discipline.num_mans})
        )

    return JsonResponse(discipline_overview, safe=False)


def about(request):
    """

    Miniature view. Only relevant data is counting the number of indexed maneuvers
    """

    total_number = 208
    number = Maneuver.objects.filter(has_errata_elsewhere=False).count()
    percent_complete = int(number / total_number * 100)

    return render(
        request,
        "about.html",
        {"number": number, "total": total_number, "percent": percent_complete},
    )
