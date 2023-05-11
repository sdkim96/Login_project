from django import forms
from django.forms import formset_factory
from django.shortcuts import render
from ..models import CodeContent, TextContent, ImageContent

class BaseContentForm(forms.ModelForm):
    label = forms.IntegerField(widget=forms.HiddenInput())

class CodeContentForm(BaseContentForm):
    class Meta:
        model = CodeContent
        fields = ['code_content', 'label']

class TextContentForm(BaseContentForm):
    class Meta:
        model = TextContent
        fields = ['text_content', 'label']

class ImageContentForm(BaseContentForm):
    class Meta:
        model = ImageContent
        fields = ['image_content', 'label']

def progress_view(request):
    # Get the current goes value from the session, defaulting to 0
    goes = request.session.get('goes', 15) # 이거 나중에 바꿔야함

    CodeContentFormSet = formset_factory(CodeContentForm, extra=1)
    TextContentFormSet = formset_factory(TextContentForm, extra=1)
    ImageContentFormSet = formset_factory(ImageContentForm, extra=1)

    if request.method == 'POST':
        code_formset = CodeContentFormSet(request.POST, request.FILES, prefix='codes')
        text_formset = TextContentFormSet(request.POST, request.FILES, prefix='texts')
        image_formset = ImageContentFormSet(request.POST, request.FILES, prefix='images')

        # in progress_view function
        if code_formset.is_valid() and text_formset.is_valid() and image_formset.is_valid():
            # Assuming you want to link the content with the logged-in user
            user = request.user
            combined = []

            for form in code_formset:
                code_content = form.cleaned_data.get('code_content')
                label = form.cleaned_data.get('label', 0)  # Assign 0 if label is None
                if code_content:
                    combined.append(CodeContent(user=user, code_content=code_content, label=label, goes=goes))

            for form in text_formset:
                text_content = form.cleaned_data.get('text_content')
                label = form.cleaned_data.get('label', 0)  # Assign 0 if label is None
                if text_content:
                    combined.append(TextContent(user=user, text_content=text_content, label=label, goes=goes))

            for form in image_formset:
                image_content = form.cleaned_data.get('image_content')
                label = form.cleaned_data.get('label', 0)  # Assign 0 if label is None
                if image_content:
                    combined.append(ImageContent(user=user, image_content=image_content, label=label, goes=goes))

            combined = sorted(combined, key=lambda x: x.label)
            for content in combined:
                content.save()

            # increment goes value for the next submission
            goes += 1
            request.session['goes'] = goes
            # Redirect to a new URL, or add a message, or do something else
        else:
            # Handle the case when the forms are not valid
            pass
    else:
        code_formset = CodeContentFormSet(prefix='codes')
        text_formset = TextContentFormSet(prefix='texts')
        image_formset = ImageContentFormSet(prefix='images')

    return render(request, 'progress_write.html', {
        'code_formset': code_formset,
        'text_formset': text_formset,
        'image_formset': image_formset,
    })



