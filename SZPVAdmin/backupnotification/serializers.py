
from rest_framework import serializers
from .models import Notification, Region, Service, Host

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name']

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['ip','name']

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    region = RegionSerializer()
    service = ServiceSerializer()
    host = HostSerializer()
    class Meta:
        model = Notification
        fields = ['region', 'service', 'host', 'name','type','size','create_date']

    def create(self, validated_data):
        region_data = validated_data.pop('region', None)
        service_data = validated_data.pop('service', None)
        host_data = validated_data.pop('host', None)

        validated_data['region'] = Region.objects.get_or_create(**region_data)[0]
        validated_data['service'] = Service.objects.get_or_create(**service_data)[0]
        validated_data['host'] = Host.objects.get_or_create(**host_data)[0]

        backupnotify = Notification.objects.create(**validated_data)
        return backupnotify
