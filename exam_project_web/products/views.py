from django.shortcuts import render
from django.views import generic as views

from exam_project_web.products.models import Product


# Create your views here.


class ProductsListView(views.ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
