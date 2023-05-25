# load_bus_data.py
from django.core.management.base import BaseCommand
from myapp.models import Map_03
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Loads bus data from Excel file into the database'

    def handle(self, *args, **kwargs):
        # Load the data from Excel
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, 'data')
        filepath = os.path.join(data_dir, 'map_03.xlsx')

        df = pd.read_excel(filepath)

        # Iterate over the rows of the DataFrame and create BusStation objects
        for index, row in df.iterrows():
            map_3 = Map_03(
                longitude = row['경도'],
                latitude = row['위도'],
                province = row['중심시도명'],
                district = row['중심시군구명'],
                tourist_spot = row['중심관광지명'],
                address = row['Unnamed: 5'],
                category_large = row['중심카테고리 명_대'],
                category_medium = row['중심카테고리 명_중'],
                rank = row['순위']
            )
            map_3.save()


        self.stdout.write(self.style.SUCCESS('Successfully loaded bus data'))
