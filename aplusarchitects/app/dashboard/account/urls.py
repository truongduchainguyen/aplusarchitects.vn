from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('password/change/', views.password_change, name='password-change'),
    # Customers
    path('customers/', views.customer_list, name='customer-list'),
    path('customers/add/', views.customer_add, name='customer-add'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer-delete'),
    path('customers/<int:pk>/change/', views.customer_change, name='customer-change'),
    # Staffs
    path('staffs/', views.staff_list, name='staff-list'),
    path('staffs/add/', views.staff_add, name='staff-add'),
    path('staffs/<int:pk>/change/', views.staff_change, name='staff-change'),
    path('staffs/<int:pk>/delete/', views.staff_delete, name='staff-delete'),
]
