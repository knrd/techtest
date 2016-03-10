from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.conf import settings
import os


# naming image by name field
def upload_path(instance, filename):
    # name file as "name" form filed
    ext = filename.split('.')[-1]
    newname = instance.name + "." + ext

    # delete file if exists
    fullname = os.path.join(settings.MEDIA_ROOT, newname)
    if os.path.exists(fullname):
        os.remove(fullname)

    return newname


class Image(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # I could use ImageFiled instead, but it requires Pillow lib. To make this simple I leave FileField.
    image = models.FileField(upload_to=upload_path)

    def __unicode__(self):
        return self.name


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image']
