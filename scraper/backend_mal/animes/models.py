from django.db import models
from django.conf import settings


# Create your models here.
class Anime(models.Model):
    season = models.ForeignKey(
        "seasons.Season",
        models.DO_NOTHING,
        related_name="anime",
    )
    is_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.DO_NOTHING,
        db_column="is_manager",  # 중요
        related_name="anime",
    )
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20, blank=True, null=True)
    episodes = models.CharField(max_length=10, blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    main_img = models.CharField(max_length=300, blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        managed = False
        db_table = "anime"
