from django.db import models
from jsonfield import JSONField

# Create your models here.

class Report(models.Model):
    xml_file = models.FileField(upload_to='uploads/')
    timestamp = models.DateTimeField(auto_now_add=True)


class Vehicle(models.Model):
    type = models.CharField(max_length=50)
    frame = models.CharField(max_length=20)
    power_train = models.CharField(max_length=20)
    wheels = JSONField(default=[])
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
