from rest_framework import serializers
from .models import Source, SourceList


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class MiniSourceListSerializer(serializers.ModelSerializer):
    source = SourceSerializer()

    class Meta:
        model = SourceList
        fields = ("source",)
