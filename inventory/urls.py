from django.urls import path
from .views import product_upload_view
from .views import products_list
from .views import product_detail
from.views import product_update_view
from.views import delete_product
from .views import product_upload_view


urlpatterns=[
    path("products/upload/",product_upload_view, name="product_upload_view"),

    path("products/list/", products_list, name="product_list_view"),

    path("products/<int:id>/", product_detail, name="product_description_view"),

    path("inventory/products/edit/<int:id>/",product_update_view,name="product_update"),

    path("products/delete/<int:id>/", delete_product, name="delete_product_view")
    
]