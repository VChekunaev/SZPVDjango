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
    name = models.CharField(max_length=64)

    def __str__(self):
        return ('%s - %s') % (self.name,self.ip)

class Notification(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=16)
    size = models.IntegerField()
    create_date = models.DateTimeField()

    def __str__(self):
        return ('%s - %s - %s') % (self.region.name,self.host.ip,self.backup.name)