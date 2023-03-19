from rest_framework import serializers
from .models import *


class BroadcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcast
        fields = "__all__"


class BroadcastListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroadcastList
        fields = "__all__"
