from django.urls import path

from exam_project_web.products.views import ProductsListView

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list")
]