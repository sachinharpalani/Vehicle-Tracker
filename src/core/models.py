from django.db import models
from jsonfield import JSONField
import os
from django.urls import reverse_lazy

# Create your models here.

class Report(models.Model):
    xml_file = models.FileField(upload_to='uploads/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.xml_file.name)

    def fileurl(self):
        return self.xml_file.url

    def go_to_report(self):
        return '/report/'+ str(self.id)


class Vehicle(models.Model):
    type = models.CharField(max_length=50)
    frame = models.CharField(max_length=20)
    power_train = models.CharField(max_length=20)
    wheels = JSONField(default=[])
    report = models.ForeignKey(Report,on_delete=models.CASCADE)

    def get_wheels_text(self):
        """
        This returns wheels in text format as a single string
        For eg:
        [{'position':'rear','material':'plastic'}{'position':'front','material':'plastic'}]
        will be returned as 2 plastic (rear,front)
        """
        all_m = {m["material"] for m in self.wheels}
        all_m = ' '.join(map(str,all_m))
        all_w = ','.join(map(lambda x: x["position"],self.wheels))
        wheels_text = "{no} {material} ({positions})".format(no=str(len(self.wheels)),material=str(all_m),positions=all_w)
        return wheels_text
