from django.db import models
from animes.models import Anime


# Create your models here.
class Theme(models.Model):
    id = models.BigAutoField(primary_key=True)
    theme_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.theme_name

    class Meta:
        managed = False
        db_table = "theme"


class ThemeList(models.Model):
    anime = models.OneToOneField(Anime, models.DO_NOTHING, primary_key=True)
    theme = models.ForeignKey(Theme, models.DO_NOTHING)

    def __str__(self) -> str:
        name = self.anime.title
        if len(name) > 30:
            return f"{name[:30]}... - {self.theme.theme_name}"
        else:
            return f"{name} - {self.theme.theme_name}"

    class Meta:
        managed = False
        db_table = "theme_list"
        unique_together = (("anime", "theme"),)
