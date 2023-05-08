from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def progress(request):
    return render(request, 'progress.html')

def visualization(request):
    return render(request, 'visualization.html')