from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class AnimeGenreSerializer(serializers.ModelSerializer):
    anime = ReadOnlyField(source="anime.name")
    genre = ReadOnlyField(source="genre.name")

    c_anime_genre = serializers.SerializerMethodField()
    # c_genre = serializers.SerializerMethodField()

    def get_c_anime_genre(self, x):
        return x.anime_genre()

    class Meta:
        model = AnimeGenres
        fields = "__all__"
