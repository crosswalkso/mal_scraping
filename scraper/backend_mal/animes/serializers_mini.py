from rest_framework import serializers
from .models import Anime


class MiniAnimeSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()

    def get_members(self, anime):
        return anime.members()

    def get_score(self, anime):
        return anime.score()

    class Meta:
        model = Anime
        fields = (
            "id",
            "title",
            "main_img",
            "members",
            "score",
        )
