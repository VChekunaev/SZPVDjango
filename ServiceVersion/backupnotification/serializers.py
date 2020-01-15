
from rest_framework import serializers


class BackupNotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

    region_id = serializers.IntegerField()
    service_id = serializers.IntegerField()
    backupName = serializers.CharField(max_length=256)
    eventdatetime = serializers.CharField()
    success = serializers.BooleanField()
