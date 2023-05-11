from django.shortcuts import render
from django.db.models import Max, Q
from ..models import CodeContent, TextContent, ImageContent
from django.contrib.contenttypes.models import ContentType
from myapp.models import BaseContent, CodeContent, TextContent, ImageContent
from django_plotly_dash import DjangoDash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import chardet
from .visualization.bus import get_merged_df


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from django.forms.models import model_to_dict

def progress(request):
    # Get the latest goes value from all content types
    all_contents = sorted(
        list(CodeContent.objects.filter(user=request.user)) + 
        list(TextContent.objects.filter(user=request.user)) + 
        list(ImageContent.objects.filter(user=request.user)), 
        key=lambda x: x.goes, 
        reverse=True
    )

    if not all_contents:
        whole_contents = []
        for content in all_contents:
            if content.goes == latest_goes:
                content_dict = model_to_dict(content)
                if isinstance(content, ImageContent):
                    content_dict['image_content'] = content.image_content.url
                whole_contents.append(content_dict)
        whole_contents.sort(key=lambda content: content['label'])

    else:
        latest_goes = all_contents[0].goes
        whole_contents = [content for content in all_contents if content.goes == latest_goes]
        whole_contents.sort(key=lambda content: content.label)

    # Transform the model instances into dictionaries
    whole_contents = [model_to_dict(content) for content in whole_contents]

    return render(request, 'progress.html', {
        'whole_contents': whole_contents,
    })

app = DjangoDash('BusStations', add_bootstrap_links=True)

app.layout = html.Div([
    dcc.Dropdown(
        id='top-n-stations',
        options=[{'label': i, 'value': i} for i in range(1, 31)],
        value=1
    ),
    dcc.Graph(id='bus-stations-graph')
])

@app.callback(
    Output('bus-stations-graph', 'figure'),
    [Input('top-n-stations', 'value')]
)
def update_graph(top_n):
    merged_df = get_merged_df()
    # Get the top N crowded stations
    top_stations = merged_df.nlargest(top_n, '총승객수')

    # Create a new figure and plot the data
    figure = go.Figure(
        data=[
            go.Scattergeo(
                lat=top_stations['Y좌표'],
                lon=top_stations['X좌표'],
                text=top_stations['정류소명'],
                mode='markers',
                marker=dict(
                    size=top_stations['총승객수']/100000,  # Adjust the size of markers
                    color='red',
                    opacity=0.4
                )
            )
        ]
    )

def visualization(request):
    return render(request, 'visualization.html')