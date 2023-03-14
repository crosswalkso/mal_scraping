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

    def __str__(self) -> str:
        name = self.anime.title
        if len(name) > 30:
            return f"{name[:30]}... - {self.source.source_name}"
        else:
            return f"{name} - {self.source.source_name}"

    class Meta:
        managed = False
        db_table = "source_list"
