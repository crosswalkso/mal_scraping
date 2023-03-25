from .models import DemoList
from rest_framework import serializers
from animes.serializers_mini import MiniAnimeSerializer
from .serializers_mini import DemoSerializer


class DemoListSerializer(serializers.ModelSerializer):
    anime = MiniAnimeSerializer()
    demo = DemoSerializer()

    class Meta:
        model = DemoList
        fields = "__all__"
