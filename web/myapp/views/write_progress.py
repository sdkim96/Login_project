from django import forms
from django.forms import formset_factory
from django.shortcuts import render
from ..models import CodeContent, TextContent, ImageContent, UserContent

class CodeContentForm(forms.ModelForm):
    class Meta:
        model = CodeContent
        fields = ['code_content']

class TextContentForm(forms.ModelForm):
    class Meta:
        model = TextContent
        fields = ['text_content']

class ImageContentForm(forms.ModelForm):
    class Meta:
        model = ImageContent
        fields = ['image_content']

def progress_view(request):
    CodeContentFormSet = formset_factory(CodeContentForm, extra=1)
    TextContentFormSet = formset_factory(TextContentForm, extra=1)
    ImageContentFormSet = formset_factory(ImageContentForm, extra=1)
    # FormSet definitions...

    if request.method == 'POST':
        code_formset = CodeContentFormSet(request.POST, request.FILES, prefix='codes')
        text_formset = TextContentFormSet(request.POST, request.FILES, prefix='texts')
        image_formset = ImageContentFormSet(request.POST, request.FILES, prefix='images')

        if code_formset.is_valid() and text_formset.is_valid() and image_formset.is_valid():
            user = request.user

            all_forms = list(zip(code_formset, 'Code')) + list(zip(text_formset, 'Text')) + list(zip(image_formset, 'Image'))
            all_forms.sort(key=lambda x: x[0].cleaned_data.get('order') if x[0].cleaned_data.get('order') is not None else float('inf'))

            for form, form_type in all_forms:
                if form_type == 'Code':
                    code_content = form.cleaned_data.get('code_content')
                    if code_content:
                        code = CodeContent.objects.create(user=user, code_content=code_content)
                        UserContent.objects.create(user=user, order=form.cleaned_data.get('order'), content_object=code)
                elif form_type == 'Text':
                    text_content = form.cleaned_data.get('text_content')
                    if text_content:
                        text = TextContent.objects.create(user=user, text_content=text_content)
                        UserContent.objects.create(user=user, order=form.cleaned_data.get('order'), content_object=text)
                elif form_type == 'Image':
                    image_content = form.cleaned_data.get('image_content')
                    if image_content:
                        image = ImageContent.objects.create(user=user, image_content=image_content)
                        UserContent.objects.create(user=user, order=form.cleaned_data.get('order'), content_object=image)

            # Redirect to a new URL, or add a message, or do something else
        else:
            # Handle the case when the forms are not valid
            pass
    else:
        code_formset = CodeContentFormSet(prefix='codes')
        text_formset = TextContentFormSet(prefix='texts')
        image_formset = ImageContentFormSet(prefix='images')
        # GET handling logic...

    return render(request, 'progress_write.html', {
        'code_formset': code_formset,
        'text_formset': text_formset,
        'image_formset': image_formset,
    })
