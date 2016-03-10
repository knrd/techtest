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

    return newname


class Image(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # I could use ImageFiled instead, but it requires Pillow lib. To make this simple I leave FileField.
    image = models.FileField(upload_to=upload_path, blank=False, null=False)

    def __unicode__(self):
        return self.name


class ImageForm(ModelForm):
    def save(self, dname='', *args, **kwargs):
        try:
            timg = Image.objects.get(name=dname)
            timg.image.delete(save=False)
        except: pass
        super(ImageForm, self).save(*args, **kwargs)

    class Meta:
        model = Image
        fields = ['name', 'image']
