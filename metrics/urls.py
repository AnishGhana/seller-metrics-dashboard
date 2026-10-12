from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("products/new/", views.product_create, name="product_create"),
    path("sales/new/", views.sale_create, name="sale_create"),
    path("products/<int:product_id>/delete/", views.product_delete, name="product_delete"),
]
