from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from exam_project_web.FashionForEveryone.models import Profile
from exam_project_web.products.forms import BuyProductForm
from exam_project_web.products.models import Product, BayRequest


# Create your views here.


class ProductsListView(views.ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3


def product_request(request, pk):
    if request.method == 'POST':
        form = BuyProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.to_product = Product.objects.get(id=pk)
            product.save()
            return redirect('products_list')
    else:
        form = BuyProductForm()
    return render(request, 'products/buy_product.html', {'form': form})
