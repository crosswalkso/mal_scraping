from django.db import models
from animes.models import Anime


# Create your models here.
class Broadcast(models.Model):
    id = models.BigAutoField(primary_key=True)
    broadcast_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.broadcast_name

    class Meta:
        managed = False
        db_table = "broadcast"


class BroadcastList(models.Model):
    id = models.BigAutoField(primary_key=True)
    anime = models.ForeignKey(Anime, models.DO_NOTHING)
    broadcast = models.ForeignKey(Broadcast, models.DO_NOTHING)

    def __str__(self):
        name = self.anime.title
        if len(name) > 30:
            return f"{name[:30]}... - {self.broadcast.broadcast_name}"
        else:
            return f"{name} - {self.broadcast.broadcast_name}"

    class Meta:
        managed = False
        db_table = "broadcast_list"
        unique_together = (("anime", "broadcast"),)
