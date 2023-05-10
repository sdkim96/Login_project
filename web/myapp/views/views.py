from django.shortcuts import render
from django.db.models import Max, Q
from ..models import CodeContent, TextContent, ImageContent
from django.contrib.contenttypes.models import ContentType
from myapp.models import BaseContent, CodeContent, TextContent, ImageContent


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





def visualization(request):
    return render(request, 'visualization.html')