from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

class Image(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # I could use ImageFiled instead, but it requires Pillow lib. To make this simple I leave FileField.
    image = models.FileField()

    def __unicode__(self):
        return self.name

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'image']
