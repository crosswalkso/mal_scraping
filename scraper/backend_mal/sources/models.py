from django.db import models
from animes.models import Anime


# Create your models here.
class Source(models.Model):
    id = models.BigAutoField(primary_key=True)
    source_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.source_name

    class Meta:
        managed = False
        db_table = "source"


class SourceList(models.Model):
    anime = models.OneToOneField(Anime, models.DO_NOTHING, primary_key=True)
    source = models.ForeignKey(Source, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "source_list"
