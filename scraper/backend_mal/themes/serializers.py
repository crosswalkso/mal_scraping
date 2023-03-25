from rest_framework.serializers import ModelSerializer
from .models import ThemeList
from animes.serializers_mini import MiniAnimeSerializer
from .serializers_mini import ThemeSerializer


class ThemeListSerializer(ModelSerializer):
    anime = MiniAnimeSerializer()
    theme = ThemeSerializer()

    class Meta:
        model = ThemeList
        fields = "__all__"
