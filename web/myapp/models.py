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

class Map_00(models.Model):
    total_ridership = models.IntegerField()
    route_number = models.CharField(max_length=200)
    standard_bus_station_id = models.IntegerField()
    station_name = models.CharField(max_length=200)
    x_coord = models.FloatField()
    y_coord = models.FloatField()

class Map_01(models.Model):
    places = models.CharField(max_length=200)
    rank = models.IntegerField()
    label = models.IntegerField()
    x_coord = models.FloatField()
    y_coord = models.FloatField()

class Recommend_02(models.Model):
    hotel_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    competing_hotels_count = models.IntegerField()
    competing_hotels_min_distance = models.FloatField()
    competing_hotels_max_distance = models.FloatField()
    competing_hotels_avg_distance = models.FloatField()
    bus_stops_count = models.IntegerField()
    subway_stations_count = models.IntegerField()
    nearest_bus_stop_distance = models.FloatField()
    avg_bus_stop_distance = models.FloatField()
    nearest_subway_station_distance = models.FloatField()
    avg_subway_station_distance = models.FloatField()
    monthly_average_boarding_traffic = models.FloatField()
    monthly_average_alighting_traffic = models.FloatField()
    monthly_total_traffic = models.FloatField()
    tourist_spots_count = models.IntegerField()
    shopping_malls_count = models.IntegerField()
    nearest_tourist_spot_distance = models.FloatField()
    avg_tourist_spot_distance = models.FloatField()
    nearest_shopping_mall_distance = models.FloatField()
    avg_shopping_mall_distance = models.FloatField()
    

