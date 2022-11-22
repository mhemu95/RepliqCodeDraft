from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('asset/', views.AssetTypeView.as_view(), name='asset'),
    path('employee/', views.EmployeeView.as_view(), name='employee'),
    path('tracker/', views.TrackerView.as_view(), name='tracker'),
    path('inventory/', views.IntentoryView.as_view(), name='inventory'),
]
