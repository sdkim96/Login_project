from django.shortcuts import render, redirect
from django.contrib import messages

from .visualizations.maps.map_00 import map, app
from .visualizations.maps.map_01 import map_01


def visualization(request):
    if not request.user.is_authenticated:
        messages.warning(request, '권한이 없습니다. 로그인하시고 접속해주세요.')
        return redirect('login')
    
    return render(request, 'visualization.html')
