from django.urls import path
from . import views

urlpatterns = [
    # Manage Category
    path('category/', views.category_list, name='category-list'),
    path('category/add/', views.category_add, name='category-add'),
    path('category/<int:pk>/change/', views.category_change, name='category-change'),
    path('category/<int:pk>/delete/', views.category_delete, name='category-delete'),
    # Manage Tag
    path('tag/', views.tag_list, name='tag-list'),
    path('tag/add/', views.tag_add, name='tag-add'),
    path('tag/<int:pk>/change/', views.tag_change, name='tag-change'),
    path('tag/<int:pk>/delete/', views.tag_delete, name='tag-delete'),
    # Manage Post
    path('post/', views.post_list, name='post-list'),
    path('post/add/', views.post_add, name='post-add'),
    path('post/<int:pk>/change/', views.post_change, name='post-change'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
]
