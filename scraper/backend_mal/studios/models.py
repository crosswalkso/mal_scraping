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

    class Meta:
        managed = False
        db_table = "anime_studios"
        unique_together = (("anime", "studio"),)
