import string
from django.shortcuts import render, get_object_or_404
from search_engine.forms import SearchForm
from search_engine.models import Maneuver, Discipline


def index(request):
    if request.method == 'POST':
        incoming = request.POST
        form = SearchForm(incoming)
    else:
        incoming = False
        form = SearchForm()

    # Maneuver list
    ml = Maneuver.objects
    ml = ml.filter(has_errata_elsewhere=False)

    if incoming:
        name = incoming["maneuver_name"]
        if len(name) > 0:
            ml = ml.filter(name__icontains=name)

        if "level" in incoming:
            ml = ml.filter(level__in=incoming.getlist("level"))

        if "discipline" in incoming:
            ml = ml.filter(discipline__name__in=incoming.getlist("discipline"))

        if "requirements" in incoming:
            ml = ml.filter(requirements__in=incoming.getlist("requirements"))

    number = ml.count()

    return render(request, "search.html",
                  {"form": form, "maneuvers": ml.all(), "number": number})


def maneuver(request, man_slug):
    the_maneuver = get_object_or_404(Maneuver, slug=man_slug)
    available_to = the_maneuver.discipline.initiator_classes.all()
    descriptors = the_maneuver.descriptor.all()

    return render(request, "maneuver.html",
                  {"maneuver": the_maneuver, "initiator_classes": available_to,
                   "descriptors": descriptors})


def about(request):
    number = Maneuver.objects.filter(has_errata_elsewhere=False).count()
    return render(request, "about.html", {"number": number})


def maneuvers_alphabetical(request):

    alphabet = string.ascii_uppercase

    maneuver_bag = {}
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

    return render(request, "maneuvers_alphabetical.html", {"maneuver_chunks": chunks, "title": "Alphabetical Maneuver Index", "alphabet": alphabet})


def maneuvers_by_discipline(request):
    disciplines = Discipline.objects.all()

    return render(request, "maneuvers_by_discipline.html", {"disciplines": disciplines})


def maneuvers_by_level(request):
    levels = range(1, 10)
    disciplines = Discipline.objects.all()

    maneuvers = {}
    for level in levels:
        maneuvers_of_level = Maneuver.objects.filter(level=level, has_errata_elsewhere=False)
        sublist = {}
        for discipline in disciplines:
            sublist[discipline] = maneuvers_of_level.filter(discipline=discipline).all()
        maneuvers[level] = sublist

    print(maneuvers)


    return render(request, "maneuvers_by_level.html", {"maneuvers": maneuvers, "disciplines": disciplines})