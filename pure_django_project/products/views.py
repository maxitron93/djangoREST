# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from .models import Product, Manufacturer
#
# # Create your views here.
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/products_list.html'

from django.http import JsonResponse
from django.views.generic.list import ListView
from .models import Product, Manufacturer

def products_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values('pk', 'name'))}
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {'product': {
            'name': product.name,
            'photo': product.photo.url,
            'price': product.price,
            'shipping_cost': product.shipping_cost,
            'quantity': product.quantity,
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'Product not found'
            }
        })

    return response

def manufacturers_list(request):
    try:
        manufacturers = Manufacturer.objects.filter(active=True)
        data = {'manufacturers': list(manufacturers.values('pk', 'name', 'location'))}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'No manufacturers found'
            }
        })

    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        products = Product.objects.filter(manufacturer=manufacturer)
        data = {
            'manufacturer': {
                'pk': manufacturer.pk,
                'name': manufacturer.name,
                'location': manufacturer.location,
                'active': manufacturer.active,
            },
            'products': list(products.values('pk', 'name', 'price', 'quantity'))
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'Manufacturer not found'
            }
        })

    return response