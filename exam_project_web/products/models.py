from django.db import models

# Create your models here.


class Product(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    )
    GENRE_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES)
    quantity = models.PositiveIntegerField()
    img = models.ImageField(upload_to='product_images')
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
