from django.urls import path
from .views import index
from graph import views

urlpatterns = [
    path('',index),
    path('device-data/', views.device_data, name = "device-data"),
    path('all-device/', views.all_device, name = "all-device"),
    path('device-details/<str:device_id>/', views.one_device, name = "device-details")
]
