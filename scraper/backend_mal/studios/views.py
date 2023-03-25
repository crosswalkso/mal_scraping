from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Studio, AnimeStudios
from .serializers_mini import StudioSerializer
from .serializers import StudioListSerializer

# Create your views here.


class Studios(APIView):
    def get(self, request):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 10
        start = (page - 1) * page_size
        end = start + page_size
        studios = Studio.objects.all()[start:end]
        serializer = StudioSerializer(studios, many=True)
        return Response(serializer.data)


class StudioAnimes(APIView):
    def get(self, request, studio_pk):
        anime_by_studio = AnimeStudios.objects.all().filter(studio_id=studio_pk)
        serializer = StudioListSerializer(anime_by_studio, many=True)
        return Response(serializer.data)
