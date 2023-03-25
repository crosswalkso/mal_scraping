from .models import SourceList
from rest_framework import serializers
from animes.serializers_mini import MiniAnimeSerializer
from .serializers_mini import SourceSerializer


class SourceListSerializer(serializers.ModelSerializer):
    anime = MiniAnimeSerializer()
    source = SourceSerializer()

    class Meta:
        model = SourceList
        fields = "__all__"
