from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'imageapp'
urlpatterns = [
    url(r'^$', views.main_form, name='index'),
    url(r'^image/(?P<slug>[\w_-]+)$', views.ImageDetailView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
