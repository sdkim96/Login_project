from myapp.models import Recommend_02new
from django.views.static import serve
from django.db.models.signals import post_save
from django.dispatch import receiver
import folium, os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import mpld3

from sklearn.metrics.pairwise import haversine_distances
from sklearn.cluster import DBSCAN
from sklearn.cluster import OPTICS
from sklearn.cluster import cluster_optics_dbscan
import matplotlib.gridspec as gridspec
from sklearn import datasets

from sklearn.cluster import KMeans
from scipy.stats import gaussian_kde
from sklearn.cluster import KMeans
from django_pandas.io import read_frame
import pandas as pd



colors = ['#E31B25', '#BCBDBD', '#F9D72A', '#26A59A', '#529FCD', '#FABD9E', '#FDBF6F', '#7FC97F', '#CAB2D6', '#FFFFB3',
          '#FF7F00', '#FB9A99', '#33A02C', '#B2DF8A', '#1F78B4']
bar_label = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen']


map_01_data_qs = Recommend_02new.objects.all()
map_01_data = read_frame(map_01_data_qs)
X = map_01_data[['latitude', 'longitude']].values
n_clusters = 15
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_

densities = []
for i in range(n_clusters):
    group = X[kmeans.labels_ == i]
    density = gaussian_kde(group.T)(group.T)
    densities.append(np.mean(density))

df_plt = pd.DataFrame({'label': bar_label, 'density': densities, 'color2' : colors})
df_plt = df_plt.sort_values('density', ascending=False)

print(df_plt)

def create_bar0():
    # Convert the 'label' variable to a string
    df_plt['label'] = df_plt['label'].astype(str)
    colors = df_plt['color2'].tolist()

    plt.figure(figsize=(10,8))
    ax = sns.barplot(x='label', y='density', data=df_plt, palette=colors, order=df_plt['label'])

    # Add value annotations to each bar
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

    plt.title('Density for Clusters', fontsize=12)

    # Return the plot as HTML
    return mpld3.fig_to_html(plt.gcf())



def create_folium_map():
    seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12)

    for i in range(15):   
        dfs_i = map_01_data[(map_01_data['label'] == i)]
        print(densities[i], colors[i])
        for name, lat, lng in zip(dfs_i.index, dfs_i.latitude, dfs_i.longitude):
            folium.CircleMarker([lat, lng], radius=7, color=colors[i],
                                fill=True, fill_color=colors[i],
                                fill_opacity=0.1,
                                popup=i).add_to(seoul_map)

    # Save the map as an HTML file
    seoul_map.save('myapp/templates/map_02.html')

@receiver(post_save, sender=Recommend_02new)
def update_map(sender, **kwargs):
    create_folium_map()  # Call the function to create the map

def map_02(request):
    map_file_path = 'myapp/templates/map_02.html'
    return serve(request, os.path.basename(map_file_path), os.path.dirname(map_file_path))
