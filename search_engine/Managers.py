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
