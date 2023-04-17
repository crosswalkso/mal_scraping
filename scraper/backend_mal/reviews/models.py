from django.db import models
from django.conf import settings

# Create your models here.


class Review(models.Model):
    SCORE_CHOICES = [
        (10, "10"),
        (9, "9"),
        (8, "8"),
        (7, "7"),
        (6, "6"),
        (5, "5"),
        (4, "4"),
        (3, "3"),
        (2, "2"),
        (1, "1"),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    anime = models.ForeignKey(
        "animes.Anime",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    comment = models.TextField()
    rating = models.PositiveIntegerField(
        choices=SCORE_CHOICES,
        default="10",
    )

    def __str__(self):
        return f"{self.anime} / {self.rating} - {self.user}"
