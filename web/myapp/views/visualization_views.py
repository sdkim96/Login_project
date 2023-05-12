from django.shortcuts import render
from django.views.static import serve
from myapp.models import BusData
from django_plotly_dash import DjangoDash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import chardet
import folium, os

app = DjangoDash('BusStations', add_bootstrap_links=True)

def create_folium_map(bus_data, top_n):
    # Create a new folium map
    map_folium = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

    # Add markers to the map
    for bus in bus_data:
        folium.Marker([bus.y_coord, bus.x_coord], popup=bus.station_name).add_to(map_folium)

    # Save the map as an HTML file
    map_folium.save('myapp/templates/map.html')

# Check if the map file exists, if not, create a default one
map_file_path = 'myapp/templates/map.html'
if not os.path.exists(map_file_path):
    map_folium = folium.Map(location=[37.5665, 126.9780], zoom_start=10)
    map_folium.save(map_file_path)

def map(request):
    map_file_path = 'myapp/templates/map.html'
    return serve(request, os.path.basename(map_file_path), os.path.dirname(map_file_path))

app.layout = html.Div([
    dcc.Dropdown(
        id='top-n-stations',
        options=[{'label': i, 'value': i} for i in range(1, 31)],
        value=1
    ),
    html.Iframe(id='map', srcDoc=open(map_file_path, 'r', encoding='utf-8').read(), width='100%', height='600')

])

@app.callback(
    Output('map', 'srcDoc'),
    [Input('top-n-stations', 'value')]
)
def update_map(top_n):
    bus_data = BusData.objects.order_by('-total_ridership')[:top_n]
    create_folium_map(bus_data, top_n)
    return open(map_file_path, 'r', encoding='utf-8').read()

def visualization(request):
    return render(request, 'visualization.html')