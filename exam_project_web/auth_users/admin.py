from django.contrib import admin

from exam_project_web.auth_users.models import AppUser


# Register your models here.


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ["email", "is_staff"]
    list_filter = ["email", "is_staff"]
