from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Image, ImageForm
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views import generic

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

            info = {}
            info['direct_link'] = settings.MEDIA_URL + form.cleaned_data['name'] + "." + form.cleaned_data['image'].name.split('.')[-1]
            info['detail_link'] = reverse('imageapp:detail', args=(form.cleaned_data['name'],))
            if obj:
                info['message'] = form.cleaned_data['name'] + " image changed"
            else:
                info['message'] = form.cleaned_data['name'] + " image uploaded"

            return render(request, 'imageapp/success.html', info)
            # return HttpResponseRedirect('/success/url/')
    else:
        form = ImageForm()
    return render(request, 'imageapp/mainform.html', {'formset': form})

class ImageDetailView(generic.DetailView):
    template_name = 'imageapp/detail.html'
    model = Image
    slug_field = 'name'
