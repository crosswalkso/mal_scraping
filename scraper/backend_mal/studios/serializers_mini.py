from rest_framework import serializers
from .models import Studio, AnimeStudios


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = "__all__"


class MiniStudioListSerializer(serializers.ModelSerializer):
    studio = StudioSerializer()

    class Meta:
        model = AnimeStudios
        fields = ("studio",)
