from django.contrib import admin

from exam_project_web.products.models import Product


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

