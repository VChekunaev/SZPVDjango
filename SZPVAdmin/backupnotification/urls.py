
from django.urls import path
from .views import NotificationView, RegionView, ServiceView


app_name = "backups"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('backup', NotificationView.as_view()),
    path('region', RegionView.as_view()),
    path('service', ServiceView.as_view())
]