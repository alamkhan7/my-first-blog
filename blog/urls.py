from django.conf.urls import url
from . import views
#Here were importing Djangos function url and all of our views from the blog application


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]