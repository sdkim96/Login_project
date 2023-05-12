# load_bus_data.py
from django.core.management.base import BaseCommand
from myapp.models import Map_1
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Loads bus data from Excel file into the database'

    def handle(self, *args, **kwargs):
        # Load the data from Excel
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, 'data')
        filepath = os.path.join(data_dir, 'map_1.xlsx')

        df = pd.read_excel(filepath)

        # Iterate over the rows of the DataFrame and create BusStation objects
        for index, row in df.iterrows():
            map_1 = Map_1(
                places=row['중심관광지명'],
                rank=row['순위'],
                label=row['label'],
                x_coord=row['경도'],
                y_coord=row['위도'],
            )
            map_1.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded bus data'))
