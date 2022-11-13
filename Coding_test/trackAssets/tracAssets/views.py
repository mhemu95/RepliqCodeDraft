from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AssetCategory, AssetType, Employee, AssetTracks
from .serializers import AssetTypeSerializer, EmployeeSerializer, AssetTracksSerializer


class AssetTypeView(APIView):
    def get(self, request):
        asset_type = AssetType.objects.filter(active=True)
        serializer = AssetTypeSerializer(asset_type, many=True)
        return Response({'status':'success', 'payload':serializer.data})


class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({'status':'success', 'payload':serializer.data})


class TrackerView(APIView):
    def get(self, request):
        Tracker = AssetTracks.objects.all()
        serializer = AssetTracksSerializer(Tracker, many=True)
        return Response({'status':'success', 'payload':serializer.data})
