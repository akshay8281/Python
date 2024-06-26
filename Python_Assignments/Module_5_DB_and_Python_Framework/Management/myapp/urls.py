from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/add_product/', views.add_product, name='add_product'),
    path('admin/add_product_sub_category/', views.add_product_sub_category, name='add_product_sub_category'),
    path('admin/edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('product_manager/dashboard/', views.product_manager_dashboard, name='product_manager_dashboard'),
    path('product_manager/search/', views.search_product, name='search_product'),
]
