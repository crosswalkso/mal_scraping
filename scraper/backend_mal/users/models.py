from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# -ing
class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None, gender="female"):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        name = self.model.normalize_username(name)
        user = self.model(email=email, username=name, gender=gender)
        user.set_password(password)
        user.save(using=self.db)
        return user


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
    objects = UserManager()

    def mylist(self):
        my_animes = []
        for my_anime in self.mylists.animes.values_list("id"):
            my_animes.append(my_anime[0])
        return my_animes
