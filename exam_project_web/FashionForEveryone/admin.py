from django.contrib import admin

from exam_project_web.FashionForEveryone.models import News, Comment, Profile


# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "date_time_of_published", "to_photo", "to_user"]
    list_filter = ["text", "date_time_of_published", "to_photo", "to_user"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "age"]
    list_filter = ["email", "first_name", "last_name", "age"]


