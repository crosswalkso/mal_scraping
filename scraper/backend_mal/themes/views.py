from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Theme, ThemeList
from .serializers_mini import ThemeSerializer
from .serializers import ThemeListSerializer

# Create your views here.


class Themes(APIView):
    def get(self, request):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 10
        start = (page - 1) * page_size
        end = start + page_size
        themes = Theme.objects.all()[start:end]
        serializers = ThemeSerializer(themes, many=True)
        return Response(serializers.data)


class ThemeAnimes(APIView):
    def get(self, request, theme_pk):
        anime_by_theme = ThemeList.objects.all().filter(theme_id=theme_pk)
        serializers = ThemeListSerializer(anime_by_theme, many=True)
        return Response(serializers.data)
