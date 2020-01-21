
from django.urls import path
from .views import BackupNotificationView, RegionView, ServiceView


app_name = "backups"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('backup', BackupNotificationView.as_view()),
    path('region', RegionView.as_view()),
    path('service', ServiceView.as_view())
]