from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Source, SourceList
from .serializers_mini import SourceSerializer
from .serializers import SourceListSerializer

# Create your views here.


class Sources(APIView):
    def get(self, request):
        sources = Source.objects.all().order_by("source_name")
        serializers = SourceSerializer(sources, many=True)
        return Response(serializers.data)


class SourceAnimes(APIView):
    def get(self, request, source_pk):
        anime_by_source = SourceList.objects.all().filter(source_id=source_pk)
        serializer = SourceListSerializer(anime_by_source, many=True)
        return Response(serializer.data)
