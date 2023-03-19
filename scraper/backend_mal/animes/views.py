from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Anime
from seasons.models import Season
from .serializers import AnimeSerializer


# Create your views here.
class Animes(APIView):
    # request주면 에러
    def get_season_object(self, pk):
        try:
            return Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            raise NotFound

    def get(self, request, season_pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 10
        start = (page - 1) * page_size
        end = start + page_size
        season = self.get_season_object(season_pk)
        serializer = AnimeSerializer(
            season.anime.all()[start:end],
            many=True,
        )
        return Response(serializer.data)
