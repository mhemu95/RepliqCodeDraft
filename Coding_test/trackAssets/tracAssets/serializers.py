from rest_framework import serializers
from .models import AssetType, Employee, AssetTracks

class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'

    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AssetTracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetTracks
        fields = '__all__'
