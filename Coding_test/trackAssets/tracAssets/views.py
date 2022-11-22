from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AssetCategory, AssetType, Employee, AssetTracks, Inventory
from .serializers import AssetTypeSerializer, EmployeeSerializer, AssetTracksSerializer, InventorySerializer


def home(request):

    return render(request, 'front/home.html')


class AssetTypeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'front/assets.html'

    def get(self, request):
        queryset = AssetType.objects.filter(active=True)
        return Response({'assets': queryset})

        # asset_type = AssetType.objects.filter(active=True)
        # serializer = AssetTypeSerializer(asset_type, many=True)
        # return Response({'status':'success', 'payload':serializer.data})

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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'front/tracker.html'

    def get(self, request):
        Tracker = AssetTracks.objects.all()
        return Response({'tracker': Tracker})

        #serializer = AssetTracksSerializer(Tracker, many=True)
        return Response({'status':'success', 'payload':serializer.data})

    def post(self, request):
        serializer = AssetTracksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'message':'data posted successfully'})


class IntentoryView(APIView):
    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        if inventory.count() < 1 :
            return Response({'status':'success', 'payload':'Inventory is zero'})

        return Response({'status':'success', 'payload':serializer.data})

    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'message':'data posted successfully'})    
