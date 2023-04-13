from django.db import models
from animes.models import Anime

# Create your models here.


class AnimeMembersHist(models.Model):
    d_date = models.DateField(primary_key=True)
    anime = models.ForeignKey(
        Anime,
        models.DO_NOTHING,
        related_name="membershist",
    )
    members = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "anime_members_hist"
        unique_together = (("d_date", "anime"),)


class AnimeScoreHist(models.Model):
    d_date = models.DateField(primary_key=True)
    anime = models.ForeignKey(
        Anime,
        models.DO_NOTHING,
        related_name="scorehist",
    )
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "anime_score_hist"
        unique_together = (("d_date", "anime"),)
