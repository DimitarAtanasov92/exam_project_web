from django.urls import path, include

from exam_project_web.FashionForEveryone.views import home

urlpatterns = [
    path("", home, name="index"),
]