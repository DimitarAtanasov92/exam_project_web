from django.contrib import admin

from exam_project_web.FashionForEveryone.models import News


# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]


admin.site.register(News, NewsAdmin)
