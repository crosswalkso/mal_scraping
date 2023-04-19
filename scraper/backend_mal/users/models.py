from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    is_manager = models.BooleanField(default=False)
    avatar = models.URLField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        default="Male",
    )

    def mylist(self):
        my_animes = []
        for my_anime in self.mylists.animes.values_list("id"):
            my_animes.append(my_anime[0])
        return my_animes
