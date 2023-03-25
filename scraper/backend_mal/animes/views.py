from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from .models import Anime
from seasons.models import Season
from .serializers import AnimeSerializer


# Create your views here.


# for season
# [get] api/v1/seasons/season_pk/animes
class SeasonAnimes(APIView):
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


# [get, put] api/v1/seasons/season_pk/animes/anime_pk
class SeasonAnimeDetail(APIView):
    def get_season_object(self, season_pk):
        try:
            return Season.objects.get(pk=season_pk)
        except Season.DoesNotExist:
            raise NotFound

    def get_anime_object(self, season, anime_pk):
        try:
            return season.anime.get(pk=anime_pk)
        except Anime.DoesNotExist:
            raise NotFound

    def get(self, request, season_pk, anime_pk):
        season = self.get_season_object(season_pk)
        anime = self.get_anime_object(season, anime_pk)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)

    def put(self, request, season_pk, anime_pk):
        season = self.get_season_object(season_pk)
        anime = self.get_anime_object(season, anime_pk)
        # 수정 manager만 수정 가능
        if request.user.is_authenticated and anime.is_manager == request.user:
            serializer = AnimeSerializer(
                anime,
                data=request.data,
                partial=True,
            )
            if serializer.is_valid():
                season_id = request.data.get("season")["id"]
                if not season_id:
                    raise ParseError
                try:
                    season_requested = Season.objects.get(pk=season_id)
                except Season.DoesNotExist:
                    raise ParseError
                updated_anime = serializer.save(
                    is_manager=request.user,
                    season=season_requested,
                )
                serializer = AnimeSerializer(updated_anime)
                return Response(serializer.data)
        else:
            raise NotAuthenticated
