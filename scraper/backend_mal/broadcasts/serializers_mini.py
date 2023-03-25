from rest_framework import serializers
from .models import BroadcastList
from .serializers import BroadcastSerializer


class MiniBroadcastListSerializer(serializers.ModelSerializer):
    broadcast = BroadcastSerializer()

    class Meta:
        model = BroadcastList
        fields = ("broadcast",)
