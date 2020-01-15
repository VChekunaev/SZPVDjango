"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Services(models.Model):
    serviceName = models.CharField(max_length=64)

class Regions(models.Model):
    regionName = models.CharField(max_length=64)
    regionCode = models.IntegerField()
    regionDescription = models.TextField()

class GetVersionXML(models.Model):
    rervice = models.ForeignKey(Services, on_delete=models.CASCADE)
    xml = models.TextField()

class ServiceWSDLURL(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    url = models.URLField()

class GetVersionParams:
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    url = models.ForeignKey(ServiceWSDLURL, on_delete=models.CASCADE)
    xml = models.ForeignKey(GetVersionXML,on_delete=models.CASCADE)

