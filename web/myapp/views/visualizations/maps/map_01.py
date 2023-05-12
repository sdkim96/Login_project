from myapp.models import Map_01
from django.views.static import serve
from django.db.models.signals import post_save
from django.dispatch import receiver
import folium, os

colors = ['#E31B25', '#BCBDBD', '#F9D72A', '#26A59A', '#529FCD', '#FABD9E', '#FDBF6F', '#7FC97F', '#CAB2D6', '#7FC97F']

def create_folium_map():
    # Get the data from the database
    map_01_data = Map_01.objects.all()

    # Create a new folium map
    map_folium = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

    # Add markers to the map
    for marker in map_01_data:
        color = colors[marker.label]
        folium.CircleMarker([marker.y_coord, marker.x_coord], radius=7, color=color, fill=True, fill_color=color, fill_opacity=0.1, popup=marker.places).add_to(map_folium)

    # Save the map as an HTML file
    map_folium.save('myapp/templates/map_01.html')

@receiver(post_save, sender=Map_01)
def update_map(sender, **kwargs):
    create_folium_map()  # Call the function to create the map

def map_01(request):
    map_file_path = 'myapp/templates/map_01.html'
    return serve(request, os.path.basename(map_file_path), os.path.dirname(map_file_path))
