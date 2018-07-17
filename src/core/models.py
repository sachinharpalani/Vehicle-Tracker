from django.db import models
from jsonfield import JSONField

# Create your models here.

class Vehicle(models.Model):
    type = models.CharField(max_length=50)
    frame = models.CharField(max_length=20)
    power_train = models.CharField(max_length=20)
    wheels = JSONField(default=[])

    def __str__(self):
        return self.type
