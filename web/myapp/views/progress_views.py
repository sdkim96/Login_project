from django.forms.models import model_to_dict
from myapp.models import CodeContent, TextContent, ImageContent, BaseContent
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

def progressing(request):
    if not request.user.is_authenticated:
        messages.warning(request, '권한이 없습니다. 로그인하시고 접속해주세요.')
        return redirect('login')
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