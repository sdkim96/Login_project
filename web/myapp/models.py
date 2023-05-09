from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class MyUser(AbstractUser):
    pass

class UserContent(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['order']

class CodeContent(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    code_content = models.TextField()
    submit = models.IntegerField(default=0)
    label = models.IntegerField(null=True, blank=True)

class TextContent(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text_content = models.TextField()
    submit = models.IntegerField(default=0)
    label = models.IntegerField(null=True, blank=True)

class ImageContent(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image_content = models.ImageField(upload_to='images/')
    submit = models.IntegerField(default=0)
    label = models.IntegerField(null=True, blank=True)
