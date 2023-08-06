from django.db import models
from exam_project_web.auth_users.models import AppUser
from django.contrib.auth import get_user_model
# Create your models here.


UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

