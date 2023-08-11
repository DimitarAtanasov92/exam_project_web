from django.contrib import admin

from exam_project_web.suport.models import UserSupportRequest


# Register your models here.


@admin.register(UserSupportRequest)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'email']
    list_filter = ['title', 'description', 'email']
