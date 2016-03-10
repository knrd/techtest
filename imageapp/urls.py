from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'imageapp'
urlpatterns = [
    url(r'^$', views.main_form, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
