from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated
from .models import Season
from .serializers import SeasonSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST


# Create your views here.


# [get, post, post_auth_x] api/v1/seasons/
class Seasons(APIView):
    def get(self, request):
        seasons = Season.objects.all()
        serializer = SeasonSerializer(
            seasons,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
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


# [get, put, put_auth_ing] api/v1/seasons/season_pk
# auth -> manager..
class SeasonDetail(APIView):
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
        if request.user.is_authenticated:
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
