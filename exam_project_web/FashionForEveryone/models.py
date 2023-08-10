from django.core.validators import MinLengthValidator
from django.db import models
from exam_project_web.auth_users.models import AppUser
from django.contrib.auth import get_user_model
# Create your models here.


UserModel = get_user_model()


class Profile(models.Model):
    email = models.EmailField(
        null=False, blank=False,
        unique=True
    )
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to="user_img/", blank=True, null=True)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class News(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    description = models.TextField()
    img = models.ImageField(upload_to="news_img/")


class Comment(models.Model):
    text = models.TextField(max_length=2000)
    date_time_of_published = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(News, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_published']


