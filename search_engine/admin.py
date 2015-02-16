from django.contrib import admin
from search_engine import models

admin.site.register(models.ManeuverType)
admin.site.register(models.Descriptor)
admin.site.register(models.InitiatorClass)
admin.site.register(models.Action)
admin.site.register(models.Range)
admin.site.register(models.Target)
admin.site.register(models.Area)
admin.site.register(models.Effect)
admin.site.register(models.Duration)
admin.site.register(models.SavingThrow)


class ManeuverAdmin(admin.ModelAdmin):
    exclude = ("slug", "html_description")  # these are auto-generated
    save_as = True


class DisciplineAdmin(admin.ModelAdmin):
    exclude = ("slug",)  # Auto-generated field

admin.site.register(models.Maneuver, ManeuverAdmin)
admin.site.register(models.Discipline, DisciplineAdmin)