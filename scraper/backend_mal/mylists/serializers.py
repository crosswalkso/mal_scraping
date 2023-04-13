from rest_framework.serializers import ModelSerializer
from animes.serializers_mini import MiniAnimeSerializer
from users.serializers import MiniUserSerializer
from .models import Mylist


class MylistSerializer(ModelSerializer):
    user = MiniUserSerializer()

    class Meta:
        model = Mylist
        fields = (
            "id",
            "name",
            "user",
        )


class MylistDetailSerializer(ModelSerializer):
    user = MiniUserSerializer()
    animes = MiniAnimeSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Mylist
        fields = "__all__"
