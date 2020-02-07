from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product, Manufacturer

# Create your views here.
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
