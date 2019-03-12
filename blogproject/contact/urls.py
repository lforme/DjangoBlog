from django.conf.urls import url
from . import views
from blog.views import IndexView

app_name = 'contact'

urlpatterns = [
    url('contact', views.post_contacts, name='contact'),
    url('postsucceed', views.get_post_succeed, name='postsucceed'),
    url('home', views.IndexView.as_view(), name='home'),
]
