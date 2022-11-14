from rest_framework import serializers
from .models import AssetType, Employee, AssetTracks

class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(AssetTypeSerializer, self).to_representation(instance)
        rep['category'] = instance.category.category_name
        return rep

    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AssetTracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetTracks
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(AssetTracksSerializer, self).to_representation(instance)
        rep['asset','taken_by'] = instance.asset.asset_model
        return rep
