
from rest_framework import serializers
from .models import BackupNotification, Region, Service, Host

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['id','name']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['name']


class BackupNotificationSerializer(serializers.HyperlinkedModelSerializer):
    region= serializers.CharField(source='region.name')
    service = serializers.CharField(source='service.name')
    ip = serializers.CharField(source='host.ip')
    class Meta:
        model = BackupNotification
        fields = ['region', 'service','ip', 'size', 'name', 'eventdatetime', 'success']

class BackupNotificatoinPostSerializer(serializers.HyperlinkedModelSerializer):
    region= serializers.CharField(source='region.name')
    service = serializers.CharField(source='service.name')
    host = serializers.CharField(source='host.ip')
    class Meta:
        model = BackupNotification
        fields = ['region', 'service', 'host', 'size', 'name', 'eventdatetime', 'success']

    def create(self, validated_data):
        region, created = Region.objects.get_or_create(name=validated_data['region']['name'])
        service, created = Service.objects.get_or_create(name=validated_data['service']['name'])
        host, created = Host.objects.get_or_create(ip=validated_data['host']['ip'])
        backupnotify =  BackupNotification.objects.create(region=region,service=service,host=host,
            name=validated_data['name'],
            size=validated_data['size'],
            eventdatetime=validated_data['eventdatetime'],
            success=validated_data['success'])
        return backupnotify

class AllBackupByServiceSerializer(serializers.HyperlinkedModelSerializer):
    backups = serializers.StringRelatedField(many=True)

    class Meta:
        model = Service
        fields = ['name','backups']

class AllBackupByRegionSerializer(serializers.HyperlinkedModelSerializer):
    backups = serializers.StringRelatedField(many=True)

    class Meta:
        model = Region
        fields = ['name','backups']
