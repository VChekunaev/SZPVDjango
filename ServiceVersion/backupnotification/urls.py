
from django.urls import path
from .views import BackupNotificationView


app_name = "backups"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('backups/', BackupNotificationView.as_view()),
]