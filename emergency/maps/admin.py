from django.contrib import admin

from .models import Facility


from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'country', 'website']
    list_filter = ['country', 'services']
    date_hierarchy = 'updated_at'
    # readonly_fields = ('geolocation',)

    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},

    }