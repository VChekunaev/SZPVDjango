from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Notification)
admin.site.register(Service)
admin.site.register(Region)
admin.site.register(Host)