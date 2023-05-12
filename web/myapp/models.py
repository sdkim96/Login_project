from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class MyUser(AbstractUser):
    pass

class BaseContent(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    goes = models.IntegerField(default=0)
    label = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['label']

class CodeContent(BaseContent):
    code_content = models.TextField()

class TextContent(BaseContent):
    text_content = models.TextField()

class ImageContent(BaseContent):
    image_content = models.ImageField(upload_to='images/')

class BusData(models.Model):
    total_ridership = models.IntegerField()
    route_number = models.CharField(max_length=200)
    standard_bus_station_id = models.IntegerField()
    station_name = models.CharField(max_length=200)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
