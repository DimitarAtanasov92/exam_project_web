# Generated by Django 4.2.3 on 2023-08-09 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("FashionForEveryone", "0006_alter_news_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="to_user",
            field=models.ForeignKey(
                default=6,
                on_delete=django.db.models.deletion.CASCADE,
                to="FashionForEveryone.profile",
            ),
            preserve_default=False,
        ),
    ]