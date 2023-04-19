from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Season
from animes.models import Anime
from .serializers import SeasonSerializer
from animes.serializers import AnimeSerializer
from animes.serializers_mini import MiniAnimeSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST
from datetime import datetime


# Create your views here.


# [get, post, post_auth_x] api/v1/seasons/
class Seasons(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        seasons = Season.objects.all()
        serializer = SeasonSerializer(
            seasons,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_manager:
            serializer = SeasonSerializer(data=request.data)
            if serializer.is_valid():
                season = serializer.save()
                return Response(
                    SeasonSerializer(season).data,
                )
            else:
                return Response(
                    serializer.errors,
                    status=HTTP_400_BAD_REQUEST,
                )
        else:
            raise NotAuthenticated


# [get, put, put_auth_ing] api/v1/seasons/season_pk
# auth -> manager..
class SeasonDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            raise NotFound

    # pk name을 받음
    def get(self, request, season_pk):
        season = self.get_object(season_pk)  # complex data
        serializer = SeasonSerializer(season)  # python like data
        return Response(serializer.data)  # json, text/html

    def put(self, request, season_pk):
        season = self.get_object(season_pk)
        if request.user.is_manager:
            serializer = SeasonSerializer(
                season,
                data=request.data,  # dict, json
            )

            if serializer.is_valid():
                updated_season = serializer.save()
                return Response(
                    SeasonSerializer(updated_season).data,
                )
            else:
                return Response(
                    serializer.errors,
                    status=HTTP_400_BAD_REQUEST,
                )
        else:
            raise NotAuthenticated


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
        season = self.get_season_object(season_pk)
        serializer = AnimeSerializer(
            season.anime.all()
            .filter(membershist__d_date=datetime.now().date())
            .order_by("membershist__members")[::-1],
            many=True,
        )
        return Response(serializer.data)


# [get, put] api/v1/seasons/season_pk/animes/anime_pk
class SeasonAnimeDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

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
        if request.user.is_manager:
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
