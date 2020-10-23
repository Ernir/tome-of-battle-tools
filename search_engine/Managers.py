from django.db import models


class UniqueManeuverManager(models.Manager):
    def get_queryset(self):
        return (
            super(UniqueManeuverManager, self)
            .get_queryset()
            .filter(has_errata_elsewhere=False)
        )


class ManeuverWithErrataManager(models.Manager):
    def get_queryset(self):
        return (
            super(ManeuverWithErrataManager, self)
            .get_queryset()
            .filter(has_errata_elsewhere=True)
        )


class FullManeuverManager(models.Manager):
    def get_queryset(self):
        return (
            super(FullManeuverManager, self)
            .get_queryset()
            .select_related(
                "discipline",
                "maneuver_type",
                "action",
                "range",
                "target",
                "area",
                "effect",
                "duration",
                "alternate_version",
            )
            .prefetch_related("descriptor")
        )
