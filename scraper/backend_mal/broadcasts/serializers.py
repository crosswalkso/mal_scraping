from rest_framework import serializers
from animes.serializers_mini import MiniAnimeSerializer

from .models import *


class BroadcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcast
        fields = "__all__"


class BroadcastListSerializer(serializers.ModelSerializer):
    anime = MiniAnimeSerializer()
    broadcast = BroadcastSerializer()

    class Meta:
        model = BroadcastList
        fields = "__all__"
