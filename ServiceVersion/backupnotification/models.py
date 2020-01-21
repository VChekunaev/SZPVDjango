from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Host(models.Model):
    ip = models.GenericIPAddressField()

class BackupNotification(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    size = models.IntegerField()
    eventdatetime = models.DateTimeField()
    success = models.BooleanField()

    def __str__(self):
        return ('%s - %s - %s') % (self.region.name,self.host.ip,self.name)