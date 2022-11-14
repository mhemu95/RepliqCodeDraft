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

    def post(self, request):
        serializer = AssetTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'message':'data posted successfully'})


class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({'status':'success', 'payload':serializer.data})

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'message':'data posted successfully'})


class TrackerView(APIView):
    def get(self, request):
        Tracker = AssetTracks.objects.all()
        serializer = AssetTracksSerializer(Tracker, many=True)
        return Response({'status':'success', 'payload':serializer.data})

    def post(self, request):
        serializer = AssetTracksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'message':'data posted successfully'})
