# load_bus_data.py
from django.core.management.base import BaseCommand
from myapp.models import BusData
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Loads bus data from Excel file into the database'

    def handle(self, *args, **kwargs):
        # Load the data from Excel
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, 'data')
        filepath = os.path.join(data_dir, 'bus_df.xlsx')

        df = pd.read_excel(filepath)

        # Iterate over the rows of the DataFrame and create BusStation objects
        for index, row in df.iterrows():
            bus_station = BusData(
                total_ridership=row['총승하차인원'],
                route_number=row['노선번호'],
                standard_bus_station_id=row['표준버스정류장ID'],
                station_name=row['역명'],
                x_coord=row['X좌표'],
                y_coord=row['Y좌표']
            )
            bus_station.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded bus data'))
