from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import filters
from .models import Notification, Region, Service

from .serializers import NotificationSerializer, RegionSerializer, ServiceSerializer

class NotificationView(ListAPIView):
    serializer_class = NotificationSerializer

    def get(self, request):
        limit = request.query_params.get('limit', None)
        date_from = request.query_params.get('from', None)
        date_to = request.query_params.get('to', None)
        queryset = Notification.objects.all()
        #if date_from:
        #    queryset = queryset.filter(create_date__gte=date_from)

        serializer = NotificationSerializer(queryset, many=True)
        return Response({"result": serializer.data})

    def post(self,request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            backup_saved = serializer.save()
        return Response({"result": "Successful created record about {} backup on host {}".format(backup_saved.name,backup_saved.host.name)})


class NotificationViewNew(ListCreateAPIView):
    serializer_class = NotificationSerializer
    search_fields = ['region', 'service', 'host']
    filter_backends = (filters.SearchFilter,)
    queryset = Notification.objects.all()
    
class RegionView(ListAPIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response({"region": serializer.data})

class ServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response({"service": serializer.data})


# Create your views here.
