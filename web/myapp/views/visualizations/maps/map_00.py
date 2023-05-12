from django_plotly_dash import DjangoDash
from dash import dcc, html
from dash.dependencies import Input, Output
from myapp.models import Map_00
from django.views.static import serve
import folium, os

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


app = DjangoDash('BusStations', add_bootstrap_links=True)

app.layout = html.Div([
    dcc.Dropdown(
        id='top-n-stations',
        options=[{'label': i, 'value': i} for i in range(1, 31)],
        value=1
    ),
    html.Iframe(id='map', srcDoc=open(map_file_path, 'r', encoding='utf-8').read(), width='100%', height='600px')
])

@app.callback(
    Output('map', 'srcDoc'),
    [Input('top-n-stations', 'value')]
)
def update_map(top_n):
    bus_data = Map_00.objects.order_by('-total_ridership')[:top_n]
    create_folium_map(bus_data, top_n)
    return open(map_file_path, 'r', encoding='utf-8').read()

