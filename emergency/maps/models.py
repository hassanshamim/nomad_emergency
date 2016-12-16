from django.db import models


class Location(models.Model):
    """
    Temporary Placeholder for our hospitals etc model.
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=3, null=False, blank=False)
    services = models.TextField()
    lat = models.DecimalField('Latitude', blank=True,
                              null=True, max_digits=9, decimal_places=6)
    long = models.DecimalField('Longitude',
                               blank=True, null=True, max_digits=9, decimal_places=6)

    def __str__(self):
        return "'{}' in {}".format(self.name, self.country)
