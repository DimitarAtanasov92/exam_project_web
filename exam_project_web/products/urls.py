from django.urls import path

from exam_project_web.products import views
from exam_project_web.products.views import ProductsListView

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("products_buy/<int:pk>", views.product_request, name="products_buy")
]