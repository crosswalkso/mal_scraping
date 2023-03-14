from django.db import models
from animes.models import Anime


# Create your models here.
class Studio(models.Model):
    id = models.BigAutoField(primary_key=True)
    studio_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.studio_name

    class Meta:
        managed = False
        db_table = "studio"


class AnimeStudios(models.Model):
    anime = models.OneToOneField(Anime, models.DO_NOTHING, primary_key=True)
    studio = models.ForeignKey("Studio", models.DO_NOTHING)

    def __str__(self) -> str:
        name = self.anime.title
        if len(name) > 30:
            return f"{name[:30]}... - {self.studio}"
        else:
            return f"{name} - {self.studio}"

    class Meta:
        managed = False
        db_table = "anime_studios"
        unique_together = (("anime", "studio"),)
