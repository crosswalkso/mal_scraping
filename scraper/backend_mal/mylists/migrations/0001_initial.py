# Generated by Django 4.1.7 on 2023-03-31 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("animes", "0003_alter_anime_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mylist",
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
                ("name", models.CharField(max_length=150)),
                (
                    "animes",
                    models.ManyToManyField(related_name="mylists", to="animes.anime"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mylists",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
