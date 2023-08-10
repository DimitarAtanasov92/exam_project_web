# Generated by Django 4.2.3 on 2023-08-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("S", "Small"),
                            ("M", "Medium"),
                            ("L", "Large"),
                            ("XL", "Extra Large"),
                            ("XXL", "Double Extra Large"),
                        ],
                        max_length=4,
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                ("img", models.ImageField(upload_to="product_images")),
                (
                    "genre",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                ("description", models.TextField()),
                ("price", models.FloatField()),
            ],
        ),
    ]
