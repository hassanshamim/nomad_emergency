from django.contrib import admin
from django.contrib.gis.db import models

from .models import Facility, Language

from mapwidgets import GooglePointFieldWidget

# Register your models here.
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.PointField: {'widget': GooglePointFieldWidget}
    }


admin.site.register(Language)