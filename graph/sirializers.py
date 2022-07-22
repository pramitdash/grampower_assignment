from dataclasses import field
from rest_framework import serializers
from .models import Device,All_device

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = All_device
        fields = '__all__'       