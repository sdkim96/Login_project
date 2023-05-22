from django.core.management.base import BaseCommand
from myapp.models import Recommend_02new
import pandas as pd
import os
import numpy as np

class Command(BaseCommand):
    help = 'Loads bus data from Excel file into the database'

    def handle(self, *args, **kwargs):
        # Load the data from Excel
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, 'data')
        filepath = os.path.join(data_dir, 'recommend_02.xlsx')

        df = pd.read_excel(filepath)

        # Replace NaN values with empty string ('') in the DataFrame
        

        # Iterate over the rows of the DataFrame and create Recommend_02 objects
        for index, row in df.iterrows():
            recommend_02 = Recommend_02new(
                hotel_name=row['이름'],
                latitude=row['위도'],
                longitude=row['경도'],
                competing_hotels_count=row['경쟁업소_수(1km내)'],
                competing_hotels_min_distance=row['경쟁업소_최단거리(1km내)'],
                competing_hotels_max_distance=row['경쟁업소_최장거리(1km내)'],
                competing_hotels_avg_distance=row['경쟁업소_평균거리(1km내)'],
                bus_stops_count=row['버스정류장_수(1km내)'],
                subway_stations_count=row['지하철역_수(1km내)'],
                nearest_bus_stop_distance=row['버스정류장_최단거리(1km내)'],
                avg_bus_stop_distance=row['버스정류장_평균거리(1km내)'],
                nearest_subway_station_distance=row['지하철역_최단거리(1km내)'],
                avg_subway_station_distance=row['지하철역_평균거리(1km내)'],
                monthly_average_boarding_traffic=row['교통유동인구_월평균승차수(1km내)'],
                monthly_average_alighting_traffic=row['교통유동인구_월평균하차수(1km내)'],
                monthly_total_traffic=row['교통유동인구_월평균승하차총계(1km내)'],
                tourist_spots_count=row['관광지_수(1km내)'],
                shopping_malls_count=row['쇼핑몰_수(1km내)'],
                nearest_tourist_spot_distance=row['관광지_최단거리(1km내)'],
                avg_tourist_spot_distance=row['관광지_평균거리(1km내)'],
                nearest_shopping_mall_distance=row['쇼핑몰_최단거리(1km내)'],
                avg_shopping_mall_distance=row['쇼핑몰_평균거리(1km내)'],
                label=row['label']
            )
            recommend_02.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded bus data'))

