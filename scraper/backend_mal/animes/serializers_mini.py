from rest_framework import serializers
from .models import Anime


class MiniAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = (
            "id",
            "title",
        )
