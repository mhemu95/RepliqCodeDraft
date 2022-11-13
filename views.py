from django.shortcuts import render
from . models import AssetCategory, AssetType, Employee, AssetTracks


def home(request):
    asset_count = AssetType.objects.filter(active=True).count()
    emp_count = Employee.objects.count()
    tracker_count = AssetTracks.objects.count()

    context = {
        'asset_count' : asset_count,
        'emp_count' : emp_count,
        'tracker_count' : tracker_count
    }
    return render(request, 'asset_track/home.html', context)


def assets(request):
    asset_list = AssetType.objects.filter(active=True)

    context = {
        'asset_list': asset_list
    }
    return render(request, 'asset_track/assets.html', context)


def asset_tracker(request):
    tracker_list = AssetType.objects.filter(active=True)

    context = {
        'asset_list': asset_list
    }
    return render(request, 'asset_track/assets.html', context)
