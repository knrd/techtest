from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Image, ImageForm

def main_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
    else:
        form = ImageForm()
    return render(request, 'imageapp/mainform.html', {'formset': form})