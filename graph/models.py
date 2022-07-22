from django.db import models
from pkg_resources import require

class Device(models.Model):
    device_desc = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.device_desc

class All_device(models.Model):
    device_id = models.IntegerField(blank=True, null=True)
    device_address = models.CharField(max_length=200)
    active = models.BooleanField(default=False, blank=True, null=True)
    

    def __str__(self):
        return self.device_id