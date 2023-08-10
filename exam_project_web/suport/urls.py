from django.urls import path

from exam_project_web.suport.views import SupportCreateView

urlpatterns = [
    path("", SupportCreateView.as_view(), name="support")
]