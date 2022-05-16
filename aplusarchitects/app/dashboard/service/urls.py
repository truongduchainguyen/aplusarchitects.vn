from django.urls import path
from . import views

urlpatterns = [
    # Manage Service
    path('', views.service_list, name='service-list'),
    path('add/', views.service_add, name='service-add'),
    path('<int:pk>/change/', views.service_change, name='service-change'),
    path('<int:pk>/delete/', views.service_delete, name='service-delete'),

    # Manage Service Translation
    path('<int:service_pk>/translate/add/',
        views.service_translate_add, name='service-translate-add'),
    path('<int:service_pk>/translate/<int:pk>/change/',
        views.service_translate_change, name='service-translate-change'),
    path('<int:service_pk>/translate/<int:pk>/delete/',
        views.service_translate_delete, name='service-translate-delete'),
]
