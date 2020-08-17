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
    """
    One of the nine disciplines described in the Tome of Battle - Book of Nine Swords.
    """

    class Meta:
        model = Discipline


class ManeuverTypeType(DjangoObjectType):
    """
    A type of maneuver defined in the Tome of Battle, which affects how it interacts with some class features.
    """

    class Meta:
        model = Maneuver


class DescriptorType(DjangoObjectType):
    """
    A maneuver descriptor, supplying meta-information about a maneuver. In the book, this is denoted by brackets, e.g.
    [fire].
    """

    class Meta:
        model = Descriptor


class InitiatorClassType(DjangoObjectType):
    """
    An initiator character class, which has access to one or more disciplines.
    """

    class Meta:
        model = InitiatorClass


class ActionType(DjangoObjectType):
    """
    A D&D action type, defining the "time" it takes to use a maneuver.
    """

    class Meta:
        model = Action


class RangeType(DjangoObjectType):
    """
    The range at which a maneuver can be used. Can be a number of feet, or a definition such as "melee".
    """

    class Meta:
        model = Range


class TargetType(DjangoObjectType):
    """
    Describes a valid target for a maneuver.
    """

    class Meta:
        model = Target


class AreaType(DjangoObjectType):
    """
    The area a maneuver affects, which tends to indicate the maneuver does not have a single :class:`Target`.
    """

    class Meta:
        model = Area


class EffectType(DjangoObjectType):
    """
    The effect produced by a maneuver. Most maneuvers do not produce effects, they have a :class:`Target`.
    """

    class Meta:
        model = Effect


class DurationType(DjangoObjectType):
    """
    A description of how long the maneuver lasts. Can be "instantaneous" or reference other rules, such as those which
    last as stances do, or be expressed in terms of rounds.
    """

    class Meta:
        model = Duration


class SavingThrowType(DjangoObjectType):
    """
    A saving throw allowed by a maneuver. Most maneuvers do not allow saving throws, simply dealing damage on a hit.
    """

    class Meta:
        model = SavingThrow


class ManeuverType(DjangoObjectType):
    """
    The core entity of the search engine, the one actually being searched for. Ties together all other game concepts.
    """

    class Meta:
        model = Maneuver


class Query(graphene.ObjectType):
    all_maneuvers = graphene.List(ManeuverType)

    def resolve_all_maneuvers(root, info):
        return Maneuver.objects.all()


schema = graphene.Schema(query=Query)
