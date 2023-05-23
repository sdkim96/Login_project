import pandas as pd
from django.shortcuts import render
from myapp.models import Sankey_01  # Django model
import matplotlib as mpl
import plotly.graph_objects as go
import plotly.offline as pyo

def create_gangnam_sankey(request):
    # Fetching data from the Sankey_01 model
    inflow_data = Sankey_01.objects.filter(flow_direction_code=1)
    outflow_data = Sankey_01.objects.filter(flow_direction_code=2)
    
    region_start = [data.source_region for data in inflow_data]
    region_end = [data.source_region for data in outflow_data]
    
    for lis in region_end:
        region_start.append(lis)
    
    region_start.append('서울특별시 강남구')

    string_to_add_1 = "(유입)"
    for i in range(int(int(len(region_start)/2))):
        region_start[i] += string_to_add_1

    string_to_add = " (유출)"
    for i in range(int(len(region_start) - int(len(region_start)/2)) - 1):
        region_start[i+int(len(region_start)/2)] += string_to_add

    values = [data.inflow_outflow_Ratio for data in inflow_data][0:10]
    values_end = [data.inflow_outflow_Ratio for data in outflow_data][0:10]
    for i in values_end:
        values.append(i)
        
    print(values)
    fig = go.Figure(go.Sankey(
        arrangement = "snap",
        node = {
            "label": region_start,
            'pad':10},
        link = {
            "source": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,    20,20,20,20,20,20,20,20,20,20],
            "target": [20,20,20,20,20,20,20,20,20,20,   10,11,12,13,14,15,16,17,18,19],
            "value": values}))

    plot_div = pyo.plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


