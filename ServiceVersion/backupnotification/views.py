from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BackupNotification
from .serializers import BackupNotificationSerializer

class BackupNotificationView(APIView):
    def get(self, request):
        backups = BackupNotification.objects.all()
        serializer = BackupNotificationSerializer(backups, many=True)
        return Response({"backups": serializer.data})

    def post(self,request):
        backup = request.data.get('backup')

        serializer = BackupNotificationSerializer(data=backup)
        if serializer.is_valid(raise_exception=True):
            backup_saved = serializer.save()
        return Response({"success": "Backup '{}' created successfully".format(backup_saved.backupName)})
# Create your views here.
