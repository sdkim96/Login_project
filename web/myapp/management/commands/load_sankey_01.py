
from django.core.management.base import BaseCommand
from myapp.models import Sankey_01
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Loads bus data from Excel file into the database'

    def handle(self, *args, **kwargs):
        # Load the data from Excel
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, 'data')
        filepath = os.path.join(data_dir, 'sankey_01.xlsx')

        df = pd.read_excel(filepath)

        # Iterate over the rows of the DataFrame and create BusStation objects
        for index, row in df.iterrows():
            sankey01 = Sankey_01(
                source_region = row['유입지역명'],
                destination_Region = row['유출지역명'],
                inflow_outflow_Ratio = row['유입유출 비율'],
                flow_direction_code = row['유입/유출 구분 코드 (1:유입 / 2:유출)']
            )
            sankey01.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded bus data'))
