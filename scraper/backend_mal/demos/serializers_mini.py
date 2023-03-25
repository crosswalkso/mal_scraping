from .models import Demo, DemoList
from rest_framework import serializers


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = "__all__"


class MiniDemoListSerializer(serializers.ModelSerializer):
    demo = DemoSerializer()

    class Meta:
        model = DemoList
        fields = ("demo",)
