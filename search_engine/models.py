from django.db import models
from django.db.models import Count
from django.utils.text import slugify
from markdown import markdown
from search_engine.Managers import UniqueManeuverManager, \
    ManeuverWithErrataManager


class Discipline(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    @classmethod     # TODO make this a manager
    def by_count(cls):
        return cls.objects.filter(
            maneuvers__has_errata_elsewhere=False).annotate(
            num_mans=Count("maneuvers")).order_by("num_mans")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Discipline, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ManeuverType(models.Model):
    name = models.CharField(max_length=200)

    @classmethod
    def get_type_overview(cls):
        type_names = [man_type.name for man_type in cls.objects.all()]
        type_overview = {}
        for type_name in type_names:
            type_num = Maneuver.unique_objects.filter(
                type__name=type_name).count()
            type_ratio = int(
                type_num / Maneuver.unique_objects.count() * 100)
            type_overview[type_name.lower()] = {"num": type_num,
                                                "percent": type_ratio}

        return type_overview

    def __str__(self):
        return self.name


class Descriptor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class InitiatorClass(models.Model):
    name = models.CharField(max_length=200)
    disciplines = models.ManyToManyField(Discipline,
                                         related_name="initiator_classes")

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Range(models.Model):
    name = models.CharField(max_length=200)
    is_numeric = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Target(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Area(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Effect(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Duration(models.Model):
    description = models.CharField(max_length=200)
    is_timed = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class SavingThrow(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Maneuver(models.Model):
    name = models.CharField(max_length=200)

    discipline = models.ForeignKey(Discipline, related_name="maneuvers")
    type = models.ForeignKey(ManeuverType, related_name="maneuvers")
    descriptor = models.ManyToManyField(Descriptor, blank=True)

    level = models.IntegerField()

    requirements = models.IntegerField(default=0)

    action = models.ForeignKey(Action)

    range = models.ForeignKey(Range)

    target = models.ForeignKey(Target, blank=True, null=True)
    area = models.ForeignKey(Area, blank=True, null=True)
    effect = models.ForeignKey(Effect, blank=True, null=True)

    duration = models.ForeignKey(Duration, blank=True, null=True)

    saving_throw = models.ForeignKey(SavingThrow, blank=True, null=True)

    descriptive_text = models.TextField()  # Markdown-formatted maneuver main text

    slug = models.SlugField()
    html_description = models.TextField()
    page = models.IntegerField()

    alternate_version = models.ForeignKey("self", blank=True, null=True)
    has_errata_elsewhere = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.descriptive_text = self.descriptive_text.replace("’", "'")
        self.descriptive_text = self.descriptive_text.strip()
        self.html_description = markdown(self.descriptive_text,
                                         extensions=["tables"])
        self.html_description = self.html_description.replace("<table>",
                                                              "<table class='table'>")
        super(Maneuver, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    objects = models.Manager()
    unique_objects = UniqueManeuverManager()
    maneuvers_with_errata = ManeuverWithErrataManager()

    class Meta:
        ordering = ("name",)
