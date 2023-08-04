from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from .models import Anime
from seasons.models import Season
from .serializers import AnimeSerializer
from datetime import datetime


# Create your views here.


# [get] api/v1/animes
# member수 많은 순으로 정렬
class HomeAnimes(APIView):
    def get(self, request):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 9
        start = (page - 1) * page_size
        end = start + page_size
        animes = (
            Anime.objects.all()
            .filter(membershist__d_date="2023-07-19")
            .order_by("-membershist__members")
        )[start:end]
        serializer = AnimeSerializer(
            animes,
            many=True,
        )
        return Response(serializer.data)


##############################################################################
# Do not use


# anime_by_genre
# [get] api/v1/seasons/season_pk/animes/genre/genre_pk
class SeasonGenreAnimes(APIView):
    def get_season_object(self, pk):
        try:
            return Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            raise NotFound

    def get(self, request, season_pk, genre_pk):
        """
        season = self.get_season_object(season_pk)
        anime_by_genre = season.anime.all().filter(animegenres__genre_id=genre_pk)
        """
        anime_by_genre = Anime.objects.all().filter(animegenres__genre_id=genre_pk)
        serializer = AnimeSerializer(
            anime_by_genre,
            many=True,
        )
        return Response(serializer.data)
