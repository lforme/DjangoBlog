from django.conf.urls import url, include
from . import views

app_name = 'aboutme'

urlpatterns = [
    url('aboutme', views.get_aboutme_info, name='info'),
]
