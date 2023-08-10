from django.urls import path

from exam_project_web.FashionForEveryone import views
from exam_project_web.FashionForEveryone.views import home, NewsListView, NewsDetailView, AboutUsView

urlpatterns = [
    path("", home, name="index"),
    path("news/", NewsListView.as_view(), name="news"),
    path("news/details/<int:pk>/", NewsDetailView.as_view(), name="news_details"),
    path("news/details/<int:pk>/add_comment/", views.add_comment, name="add_comment"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
]
