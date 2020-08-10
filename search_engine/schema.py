import graphene
from graphene_django import DjangoObjectType

from search_engine.models import (
    Maneuver,
    SavingThrow,
    Discipline,
    Descriptor,
    InitiatorClass,
    Range,
    Action,
    Target,
    Area,
    Effect,
    Duration,
)


class DisciplineType(DjangoObjectType):
    class Meta:
        model = Discipline


class ManeuverTypeType(DjangoObjectType):
    class Meta:
        model = Maneuver


class DescriptorType(DjangoObjectType):
    class Meta:
        model = Descriptor


class InitiatorClassType(DjangoObjectType):
    class Meta:
        model = InitiatorClass


class ActionType(DjangoObjectType):
    class Meta:
        model = Action


class RangeType(DjangoObjectType):
    class Meta:
        model = Range


class TargetType(DjangoObjectType):
    class Meta:
        model = Target


class AreaType(DjangoObjectType):
    class Meta:
        model = Area


class EffectType(DjangoObjectType):
    class Meta:
        model = Effect


class DurationType(DjangoObjectType):
    class Meta:
        model = Duration


class SavingThrowType(DjangoObjectType):
    class Meta:
        model = SavingThrow


class ManeuverType(DjangoObjectType):
    class Meta:
        model = Maneuver


class Query(graphene.ObjectType):
    all_maneuvers = graphene.List(ManeuverType)

    def resolve_all_maneuvers(root, info):
        return Maneuver.objects.all()


schema = graphene.Schema(query=Query)
