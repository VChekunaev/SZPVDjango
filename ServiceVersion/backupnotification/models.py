from django.db import models

# Create your models here.

class Service(models.Model):
    serviceName = models.CharField(max_length=64)

    def __str__(self):
        return self.serviceName
    
class Region(models.Model):
    regionName = models.CharField(max_length=64)

    def __str__(self):
        return self.regionName


class BackupNotification(models.Model):
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    backupName = models.CharField(max_length=256)
    eventdatetime = models.DateTimeField()
    success = models.BooleanField()

    def __str__(self):
        return self.backupName