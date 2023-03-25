from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from animes.serializers_mini import MiniAnimeSerializer
from .serializers_mini import GenreSerializer
from .models import *


class AnimeGenreSerializer(serializers.ModelSerializer):
    anime = MiniAnimeSerializer()
    genre = GenreSerializer()

    class Meta:
        model = AnimeGenres
        fields = "__all__"

    # anime = ReadOnlyField(source="anime.name")
    # genre = ReadOnlyField(source="genre.name")
    # c_anime_genre = serializers.SerializerMethodField()
    # # c_genre = serializers.SerializerMethodField()

    # def get_c_anime_genre(self, another):
    #     return (another.anime_id, another.genre_id)


class MiniAnimeGenreSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = AnimeGenres
        fields = ("genre",)
