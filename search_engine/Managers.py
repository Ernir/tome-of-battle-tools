from django.db import models
from django.db.models import Count


class UniqueManeuverManager(models.Manager):
    def get_queryset(self):
        return super(UniqueManeuverManager, self). \
            get_queryset().filter(has_errata_elsewhere=False)


class ManeuverWithErrataManager(models.Manager):
    def get_queryset(self):
        return super(ManeuverWithErrataManager, self). \
            get_queryset().filter(has_errata_elsewhere=True)


# class DisciplineAnnotationManager(models.Manager):
#     def get_queryset(self):
#         return super(DisciplineAnnotationManager, self).filter(
#             maneuvers__has_errata_elsewhere=False).annotate(
#             num_mans=Count("maneuvers")).order_by("num_mans")