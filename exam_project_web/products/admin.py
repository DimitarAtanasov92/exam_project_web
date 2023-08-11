from django.contrib import admin

from exam_project_web.products.models import Product, BayRequest


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "size", "price"]
    list_filter = ["name", "size", "price"]


@admin.register(BayRequest)
class BayRequestAdmin(admin.ModelAdmin):
    list_display = ["email", "address", "complete", "to_product"]
    list_filter = ["email", "address", "complete", "to_product"]



