from django.db import models
from animes.models import Anime


# Create your models here.
class Demo(models.Model):
    id = models.BigAutoField(primary_key=True)
    demo_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.demo_name

    class Meta:
        managed = False
        db_table = "demo"


class DemoList(models.Model):
    anime = models.OneToOneField(
        Anime,
        models.DO_NOTHING,
        primary_key=True,
        related_name="demolist",
    )
    demo = models.ForeignKey(
        Demo,
        models.DO_NOTHING,
        related_name="demolist",
    )

    def __str__(self) -> str:
        return f"{self.anime} - {self.demo.demo_name}"

    class Meta:
        managed = False
        db_table = "demo_list"
