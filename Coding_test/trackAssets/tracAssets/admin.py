from django.contrib import admin
from .models import AssetType, Employee, AssetCategory, AssetTracks, Inventory


admin.site.register(AssetCategory)
admin.site.register(AssetType)
admin.site.register(Employee)
admin.site.register(AssetTracks)
admin.site.register(Inventory)
