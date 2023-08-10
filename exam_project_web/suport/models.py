from django.db import models

# Create your models here.

class UserSupportRequest(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    email = models.EmailField()
