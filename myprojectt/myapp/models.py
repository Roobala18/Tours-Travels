from django.db import models
from django.utils import timezone

class Package(models.Model):
    name = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    amount = models.IntegerField()
    destination = models.CharField(max_length=100, default="Unknown")
    start_date = models.DateField(default=timezone.now)
    duration = models.CharField(max_length=50, default="1 Day")
    pax = models.IntegerField(default=1)
    trip_id = models.CharField(max_length=50, blank=True, null=True)
    itinerary = models.TextField()

    def __str__(self):
        return self.name
