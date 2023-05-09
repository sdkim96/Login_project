from django.shortcuts import render
from ..models import CodeContent, TextContent, ImageContent

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def progress(request):
    code_contents = CodeContent.objects.filter(user=request.user)
    text_contents = TextContent.objects.filter(user=request.user)
    image_contents = ImageContent.objects.filter(user=request.user)

    return render(request, 'progress.html', {'code_contents': code_contents, 'text_contents': text_contents, 'image_contents': image_contents})

def visualization(request):
    return render(request, 'visualization.html')