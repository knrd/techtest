from django.conf.urls import url
from . import views

app_name = 'imageapp'
urlpatterns = [
    url(r'^$', views.main_form, name='index'),
]
