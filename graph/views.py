from django.shortcuts import render
from ast import Return
import imp
from urllib import response
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .sirializers import TaskSerializer, DeviceSerializer
from .models import Device, All_device

def index(request):
    return render(request, 'base.html', context={'text': 'Hello World from Django'})

@api_view(['GET'])
def device_data(request):
    tasks = Device.objects.all()
    serialize = TaskSerializer(tasks, many = True)
    return Response(serialize.data)

@api_view(['GET'])
def all_device(request):
    task = All_device.objects.all()
    serialize = DeviceSerializer(task, many = True)
    return Response(serialize.data)

@api_view(['GET'])
def one_device(request,device_id):

    task = All_device.objects.get(device_id__icontains = device_id)
    serialize = DeviceSerializer(task, many = False)
    return Response(serialize.data)
        
    
    return Response("Data Doesn't Exists!!")    


