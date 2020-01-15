from django.contrib import admin

# Register your models here.

from .models import BackupNotification,Service,Region

admin.site.register(BackupNotification)
admin.site.register(Service)
admin.site.register(Region)