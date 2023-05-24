from django.shortcuts import render, redirect
from django.contrib import messages

from .visualizations.maps.map_00 import map, app
from .visualizations.maps.map_01 import map_01
from .visualizations.maps.map_02 import map_02, create_folium_map,create_bar0
from .visualizations.maps.map_03 import map_03, create_folium_map_03, map_04
from .visualizations.etc.sankey_01 import create_gangnam_sankey


def gangnam_sankey(request):
    plot_div = create_gangnam_sankey(request)
    return render(request, "sankey_01.html", context={'plot_div': plot_div})

def visualization(request):
    if not request.user.is_authenticated:
        messages.warning(request, '권한이 없습니다. 로그인하시고 접속해주세요.')
        return redirect('login')

    create_folium_map_03()
    
    plot_html = create_bar0()
    
    plot_div = create_gangnam_sankey(request)
    return render(request, 'visualization.html', {'plot_div': plot_div, 'plot_html': plot_html})

