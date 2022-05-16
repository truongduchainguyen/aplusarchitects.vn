from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<slug>[a-z0-9-_]+?)-(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
