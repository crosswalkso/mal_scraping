from django.db import models
from animes.models import Anime


# Create your models here.
class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.genre_name

    class Meta:
        managed = False
        db_table = "genre"


class AnimeGenres(models.Model):
    # WARNINGS: OneToOneField -> ForeignKey
    anime = models.ForeignKey(
        Anime,
        models.DO_NOTHING,
        primary_key=True,
        related_name="animegenres",
    )
    genre = models.ForeignKey(
        "Genre",
        models.DO_NOTHING,
        related_name="animegenres",
    )

    def __str__(self) -> str:
        name = self.anime.title
        if len(name) > 30:
            return f"{name[:30]}... - {self.genre}"
        else:
            return f"{name} - {self.genre}"

    class Meta:
        managed = False
        db_table = "anime_genres"
        unique_together = (("anime", "genre"),)
