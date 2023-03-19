from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Season
from .serializers import SeasonSerializer


# Create your views here.
class Seasons(APIView):
    def get(self, request):
        seasons = Season.objects.all()
        serializer = SeasonSerializer(
            seasons,
            many=True,
        )
        print("success: ", seasons)
        return Response(serializer.data)


"""
class SeasonDetail(APIView):
    def get_object(self, pk):
        try:
            return Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        season = self.get_object(pk)
        serializer = SeasonSerializer(season)
        return Response(serializer.data)
"""


class SeasonDetail(APIView):
    def get_object(self, pk):
        try:
            return Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            raise NotFound

    # pk name을 받음
    def get(self, request, season_pk):
        season = self.get_object(season_pk)
        serializer = SeasonSerializer(season)
        return Response(serializer.data)
