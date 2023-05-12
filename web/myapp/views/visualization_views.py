from django.shortcuts import render
from .visualizations.maps.map_00 import map, app
from .visualizations.maps.map_01 import map_01

def visualization(request):
    return render(request, 'visualization.html')
