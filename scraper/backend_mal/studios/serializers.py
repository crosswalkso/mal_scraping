from rest_framework import serializers
from .models import AnimeStudios
from animes.serializers_mini import MiniAnimeSerializer
from .serializers_mini import StudioSerializer


class StudioListSerializer(serializers.ModelSerializer):
    anime = MiniAnimeSerializer()
    studio = StudioSerializer()

    class Meta:
        model = AnimeStudios
        fields = "__all__"
