import string
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from search_engine.forms import SearchForm
from search_engine.models import Maneuver, Discipline


def index(request):
    return render(request, "index.html")


def search(request):
    """
    Displays the main search page, to be later filled with data via AJAX.
    """
    mans = Maneuver.objects.filter(has_errata_elsewhere=False)
    return render(request, "search.html", {"form": SearchForm()})


def perform_search(request):
    """
    Generates a list of maneuvers to display based on POST parameters.
    Returns their names and slugs in JSON format.
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
                name = post_body["maneuver_name"]
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


def maneuver(request, man_slug):
    """

    Defines the page of a single maneuver.
    Finds the maneuver based on its slugified name, passed in by man_slug.
    """
    the_maneuver = get_object_or_404(Maneuver, slug=man_slug)
    available_to = the_maneuver.discipline.initiator_classes.all()
    descriptors = the_maneuver.descriptor.all()

    return render(request, "maneuver.html",
                  {"maneuver": the_maneuver, "initiator_classes": available_to,
                   "descriptors": descriptors})


def maneuvers_alphabetical(request):
    """

    Defines an alphabetical index of maneuvers.
    Returns three "chunks" of maneuvers, each to be placed in a column.
    Each chunk is a dictionary with letters of the alphabet as keys,
    and lists of all maneuvers starting with each letter as their values.
    """
    alphabet = string.ascii_uppercase

    maneuver_bag = {}
    chunk_breaks = ["F", "Q", "Z"]  # The letters where we break the columns.
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
            "alphabet": alphabet
        }
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
        maneuvers_of_level = Maneuver.objects.filter(level=level,
                                                     has_errata_elsewhere=False)
        sublist = {}
        for discipline in disciplines:
            sublist[discipline] = maneuvers_of_level.filter(discipline=discipline).all()
        maneuvers[level] = sublist

    return render(
        request,
        "maneuvers_by_level.html",
        {
            "maneuvers": maneuvers,
            "disciplines": disciplines
        }
    )


def about(request):
    """

    Miniature view, only action is to the number of completed maneuvers (without dupes).
    """
    number = Maneuver.objects.filter(has_errata_elsewhere=False).count()
    return render(
        request,
        "about.html",
        {"number": number}
    )