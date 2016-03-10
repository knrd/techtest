from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Image, ImageForm

def main_form(request):
    if request.method == 'POST':
        objname = ''
        if 'name' in request.POST:
            objname = request.POST['name']

        # I try to fetch object to update image, if object exists
        try:
            obj = Image.objects.get(name=objname)
        except Image.DoesNotExist:
            obj = None

        form = ImageForm(request.POST, request.FILES, instance=obj)
        # save changes only when new image is provided
        if form.is_valid() and request.FILES:
            form.save(dname=objname)
    else:
        form = ImageForm()
    return render(request, 'imageapp/mainform.html', {'formset': form})