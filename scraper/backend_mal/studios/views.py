from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Studio, AnimeStudios
from .serializers_mini import StudioSerializer
from .serializers import StudioListSerializer

# Create your views here.


class Studios(APIView):
    def get(self, request):
        studios = Studio.objects.all().order_by("studio_name")
        serializer = StudioSerializer(studios, many=True)
        return Response(serializer.data)


class StudioAnimes(APIView):
    def get(self, request, studio_pk):
        anime_by_studio = AnimeStudios.objects.all().filter(studio_id=studio_pk)
        serializer = StudioListSerializer(anime_by_studio, many=True)
        return Response(serializer.data)
