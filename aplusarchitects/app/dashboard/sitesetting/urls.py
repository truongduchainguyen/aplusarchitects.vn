from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('general/', views.general_information, name='general-information'),
    path('social-network/', views.social_network_list, name='social-network-list'),
    path('social-network/add/', views.social_network_add,
         name='social-network-add'),
    path('social-network/<int:pk>/change/',
         views.social_network_change, name='social-network-change'),
    path('social-network/<int:pk>/delete/',
         views.social_network_delete, name='social-network-delete'),
]
