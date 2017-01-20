from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
        postTypes = (
            ('DR', 'driver'),
            ('PA', 'passenger')
        )
        statuses = (
            ('F', 'Full'),
            ('A', 'Available')
        )
        title = models.CharField(max_length=255)
        description = models.TextField()
        timePosted = models.DateTimeField(auto_now_add=True)
        postType = models.CharField(max_length=20,choices=postTypes)
        # TODO: link creator
        origin = models.CharField(max_length=255)
        destination = models.CharField(max_length=255)
        emptySeats = models.IntegerField()
        passengerCapacity = models.IntegerField()
        status = models.CharField(max_length=20,choices=statuses)