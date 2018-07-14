from django.db import models
from haystack.utils.geo import Point


class Location(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    @property
    def coordinates(self):
        return Point(self.longitude, self.latitude)
