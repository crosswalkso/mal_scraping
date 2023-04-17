from django.db import models
from django.conf import settings

# Create your models here.


class Mylist(models.Model):
    name = models.CharField(
        max_length=150,
    )
    animes = models.ManyToManyField(
        "animes.Anime",
        related_name="mylists",
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mylists",
    )

    def __str__(self):
        return self.name
