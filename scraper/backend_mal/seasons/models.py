from django.db import models


# Create your models here.
class Season(models.Model):
    id = models.BigAutoField(primary_key=True)
    season_name = models.TextField()

    def __str__(self) -> str:
        return self.season_name

    class Meta:
        managed = False
        db_table = "season"
