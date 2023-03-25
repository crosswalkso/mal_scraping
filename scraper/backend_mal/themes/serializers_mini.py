from rest_framework.serializers import ModelSerializer
from .models import Theme, ThemeList


class ThemeSerializer(ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class MiniThemeListSerializer(ModelSerializer):
    theme = ThemeSerializer()

    class Meta:
        model = ThemeList
        fields = ("theme",)
