import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import pandas as pd
import chardet
import os

# Fetch the data from the database
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_dir = os.path.join(base_dir, 'data')

buspathraw = os.path.join(data_dir, 'buspath.xlsx')
busraw = os.path.join(data_dir, 'bus.csv')

# detect file encoding
with open(busraw, 'rb') as f:
    result = chardet.detect(f.read())
encoding = result['encoding']

# read CSV file
bus = pd.read_csv(busraw, encoding=encoding, low_memory=False)

# read Excel file
buspath = pd.read_excel(buspathraw)

bus_columns = [col for col in bus.columns if '승차총승객수' in col or '하차총승객수' in col]
bus_total = bus[['표준버스정류장ID'] + bus_columns]
# 승하차 승객수 합계 계산
bus_total['총승객수'] = bus_total[bus_columns].sum(axis=1)

# 정류장별 총 승객수 합계
station_total = bus_total.groupby('표준버스정류장ID')['총승객수'].sum().reset_index()

# 데이터프레임 병합
def get_merged_df():
    merged_df = pd.merge(station_total, buspath, left_on='표준버스정류장ID', right_on='NODE_ID')
    return merged_df
