from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base'),
    path('asset/', views.AssetTypeView.as_view()),
    path('employee/', views.EmployeeView.as_view()),
    path('tracker/', views.TrackerView.as_view()),
    path('inventory/', views.IntentoryView.as_view()),
]
