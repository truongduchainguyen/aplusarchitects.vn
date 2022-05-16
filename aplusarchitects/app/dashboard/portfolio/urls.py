from django.urls import path
from . import views

urlpatterns = [
    # Manage Category
    path('category/', views.category_list, name='category-list'),
    path('category/add/', views.category_add, name='category-add'),
    path('category/<int:pk>/change/', views.category_change, name='category-change'),
    path('category/<int:pk>/delete/', views.category_delete, name='category-delete'),

    # Manage Category Translation
    path('category/<int:category_pk>/translate/add/',
        views.category_translate_add, name='category-translate-add'),
    path('category/<int:category_pk>/translate/<int:pk>/change/',
        views.category_translate_change, name='category-translate-change'),
    path('category/<int:category_pk>/translate/<int:pk>/delete/',
        views.category_translate_delete, name='category-translate-delete'),

    # Manage Project
    path('project/', views.project_list, name='project-list'),
    path('project/add/', views.project_add, name='project-add'),
    path('project/<int:pk>/change/', views.project_change, name='project-change'),
    path('project/<int:pk>/delete/', views.project_delete, name='project-delete'),

    # Manage Project Translation
    path('project/<int:project_pk>/translate/add/',
        views.project_translate_add, name='project-translate-add'),
    path('project/<int:project_pk>/translate/<int:pk>/change/',
        views.project_translate_change, name='project-translate-change'),
    path('project/<int:project_pk>/translate/<int:pk>/delete/',
        views.project_translate_delete, name='project-translate-delete'),

    # Manage Project Image
    path('project/<int:project_pk>/images/',
        views.project_images, name='project-images-list'),
    path('project/<int:project_pk>/images/add/',
        views.project_images_add, name='project-images-add'),
    path('project/<int:project_pk>/images/<int:pk>/change/',
        views.project_images_change, name='project-images-change'),
    path('project/<int:project_pk>/images/<int:pk>/delete/',
        views.project_images_delete, name='project-images-delete'),
    path('project/<int:project_pk>/images/reorder/',
        views.project_images_reorder, name='project-images-reorder'),
]
