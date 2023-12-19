from myapp.models import Map_03
from django_pandas.io import read_frame
from sklearn.cluster import OPTICS
import numpy as np
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.views.static import serve
import os
import folium
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


def create_folium_map_03():
    map_03_data_qs = Map_03.objects.all()
    df = read_frame(map_03_data_qs)
    X = df[['latitude', 'longitude']].values

    optics = OPTICS(min_samples=5, xi=0.05, min_cluster_size=0.03, max_eps=np.inf, cluster_method='xi')

    optics.fit(X)

    cluster_labels = optics.labels_
    core_distances = optics.core_distances_

    df['label'] = cluster_labels
    df_noise = df[(df['label'] == -1)]
    df = df[(df['label'] != -1)]

    labels = np.arange(len(df['label'].unique()))

    cmap = plt.get_cmap('tab20')
    colors = [cmap(i) for i in labels % cmap.N]
    hex_colors = [mcolors.rgb2hex(color) for color in colors]

    seoul_map = folium.Map(location=[37.55, 126.98], attr='Map data © OpenStreetMap contributors', zoom_start=12)
    seoul_map2 = folium.Map(location=[37.55, 126.98], attr='Map data © OpenStreetMap contributors', zoom_start=12)

    for i in range(len(df['label'].unique())):   
        dfss = df[(df['label'] == i)]
        for name, lat, lng, tour in zip(dfss.index, dfss.latitude, dfss.longitude, dfss.tourist_spot):
            folium.CircleMarker([lat, lng], radius=7, color=hex_colors[i],
                                fill=True, fill_color=hex_colors[i],
                                fill_opacity=0.1,
                                popup=i).add_to(seoul_map)
    
    for name, lat, lng in zip(df_noise.index, df_noise.latitude, df_noise.longitude):
        folium.CircleMarker([lat, lng], radius=7, color='black',
                            fill=True, fill_color='black',
                            fill_opacity=0.1,
                            popup=i).add_to(seoul_map2)

    seoul_map.save('myapp/templates/map_03.html')
    seoul_map2.save('myapp/templates/map_04.html')
    


@receiver(post_save, sender=Map_03)
def update_map_03(sender, **kwargs):
    create_folium_map_03()

def map_03(request):
    map_file_path = 'myapp/templates/map_03.html'
    return serve(request, os.path.basename(map_file_path), os.path.dirname(map_file_path))

def map_04(request):
    map_file_path = 'myapp/templates/map_04.html'
    return serve(request, os.path.basename(map_file_path), os.path.dirname(map_file_path))
