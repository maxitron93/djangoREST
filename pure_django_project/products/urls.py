from django.urls import path
# from .views import ProductDetailView, ProductListView
from .views import products_list, product_detail, manufacturers_list, manufacturer_detail

# urlpatterns = [
#     path('', ProductListView.as_view(), name='products_list'),
#     path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail')
# ]

urlpatterns = [
    path('', products_list, name='products_list'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('manufacturers/', manufacturers_list, name='manufacturers'),
    path('manufacturer/<int:pk>', manufacturer_detail, name='manufacturer_detail'),
]