from rest_framework import serializers
from .models import Anime
from seasons.serializers import SeasonSerializer
from broadcasts.serializers_mini import MiniBroadcastListSerializer
from genres.serializers import MiniAnimeGenreSerializer
from demos.serializers_mini import MiniDemoListSerializer
from themes.serializers_mini import MiniThemeListSerializer
from sources.serializers_mini import MiniSourceListSerializer
from studios.serializers_mini import MiniStudioListSerializer


# foreignkey
# django 관리자 페이지를 위함
class AnimeSerializer(serializers.ModelSerializer):
    season = SeasonSerializer()
    broadcastlist = MiniBroadcastListSerializer(many=True, read_only=True)
    animegenres = MiniAnimeGenreSerializer(many=True, read_only=True)
    demolist = MiniDemoListSerializer(read_only=True)
    themelist = MiniThemeListSerializer(many=True, read_only=True)
    sourcelist = MiniSourceListSerializer(read_only=True)
    animestudios = MiniStudioListSerializer(read_only=True, many=True)

    class Meta:
        model = Anime
        fields = "__all__"
