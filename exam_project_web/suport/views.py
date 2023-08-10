from django.shortcuts import render
from django.views import generic as views

from exam_project_web.suport.models import UserSupportRequest


# Create your views here.


class SupportCreateView(views.CreateView):
    model = UserSupportRequest
    template_name = 'support/support.html'
    fields = ["title", "description", "email"]
