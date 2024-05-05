from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Baby)
admin.site.register(models.BabyDeparture)
admin.site.register(models.Payment)
admin.site.register(models.ProcuredItem)
admin.site.register(models.ResoldDoll)
admin.site.register(models.Sitter)
