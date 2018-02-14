from django.db import models

from django_countries.fields import CountryField
from django_google_maps import fields as map_fields


class Facility(models.Model):
    # TODO: add language field/model
    name = models.CharField(max_length=100)
    services = models.CharField(blank=True, max_length=500)
    website = models.URLField(blank=True)
    country = CountryField()
    # lat = models.DecimalField('Latitude', blank=True,
    #                           null=True, max_digits=9, decimal_places=6)
    # long = models.DecimalField('Longitude',
    #                            blank=True, null=True, max_digits=9, decimal_places=6)
    address = map_fields.AddressField(max_length=150)
    geolocation = map_fields.GeoLocationField()

    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    class Meta:
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return "'{}' in {}".format(self.name, self.country)
