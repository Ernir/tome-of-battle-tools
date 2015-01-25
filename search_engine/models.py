from django.db import models
from django.utils.text import slugify
from markdown import markdown
from markdown.extensions import tables


class Discipline(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Discipline, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ManeuverType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Descriptor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class InitiatorClass(models.Model):
    name = models.CharField(max_length=200)
    disciplines = models.ManyToManyField(Discipline, related_name="initiator_classes")

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
    type = models.ForeignKey(ManeuverType, blank=True, null=True, related_name="maneuvers")
    descriptor = models.ManyToManyField(Descriptor, blank=True, null=True)

    level = models.IntegerField()

    requirements = models.IntegerField(default=0)

    action = models.ForeignKey(Action)

    range = models.ForeignKey(Range)

    target = models.ForeignKey(Target, blank=True, null=True)
    area = models.ForeignKey(Area, blank=True, null=True)
    effect = models.ForeignKey(Effect, blank=True, null=True)

    duration = models.ForeignKey(Duration, blank=True, null=True)

    saving_throw = models.ForeignKey(SavingThrow, blank=True, null=True)

    descriptive_text = models.TextField()

    slug = models.SlugField()
    html_description = models.TextField()
    page = models.IntegerField()

    alternate_version = models.ForeignKey("self", blank=True, null=True)
    has_errata_elsewhere = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        self.html_description = markdown(self.descriptive_text, extensions=["tables"])
        self.html_description = self.html_description.replace("<table>", "<table class='table'>")
        super(Maneuver, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)