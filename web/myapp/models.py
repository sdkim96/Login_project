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

#아래 recommend_02안씀
class Recommend_02(models.Model):
    hotel_name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    competing_hotels_count = models.IntegerField(null=True)
    competing_hotels_min_distance = models.FloatField(null=True)
    competing_hotels_max_distance = models.FloatField(null=True)
    competing_hotels_avg_distance = models.FloatField(null=True)
    bus_stops_count = models.IntegerField(null=True)
    subway_stations_count = models.IntegerField(null=True)
    nearest_bus_stop_distance = models.FloatField(null=True)
    avg_bus_stop_distance = models.FloatField(null=True)
    nearest_subway_station_distance = models.FloatField(null=True)
    avg_subway_station_distance = models.FloatField(null=True)
    monthly_average_boarding_traffic = models.FloatField(null=True)
    monthly_average_alighting_traffic = models.FloatField(null=True)
    monthly_total_traffic = models.FloatField(null=True)
    tourist_spots_count = models.IntegerField(null=True)
    shopping_malls_count = models.IntegerField(null=True)
    nearest_tourist_spot_distance = models.FloatField(null=True, blank=True)
    avg_tourist_spot_distance = models.FloatField(null=True)
    nearest_shopping_mall_distance = models.FloatField(null=True)
    avg_shopping_mall_distance = models.FloatField(null=True)
    label = models.IntegerField(null=True)
    
class Recommend_02new(models.Model):
    hotel_name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    competing_hotels_count = models.IntegerField(null=True)
    competing_hotels_min_distance = models.FloatField(null=True)
    competing_hotels_max_distance = models.FloatField(null=True)
    competing_hotels_avg_distance = models.FloatField(null=True)
    bus_stops_count = models.IntegerField(null=True)
    subway_stations_count = models.IntegerField(null=True)
    nearest_bus_stop_distance = models.FloatField(null=True)
    avg_bus_stop_distance = models.FloatField(null=True)
    nearest_subway_station_distance = models.FloatField(null=True)
    avg_subway_station_distance = models.FloatField(null=True)
    monthly_average_boarding_traffic = models.FloatField(null=True)
    monthly_average_alighting_traffic = models.FloatField(null=True)
    monthly_total_traffic = models.FloatField(null=True)
    tourist_spots_count = models.IntegerField(null=True)
    shopping_malls_count = models.IntegerField(null=True)
    nearest_tourist_spot_distance = models.FloatField(null=True, blank=True)
    avg_tourist_spot_distance = models.FloatField(null=True)
    nearest_shopping_mall_distance = models.FloatField(null=True)
    avg_shopping_mall_distance = models.FloatField(null=True)
    label = models.IntegerField(null=True)
