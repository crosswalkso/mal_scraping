from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Demo, DemoList
from .serializers import DemoListSerializer
from .serializers_mini import DemoSerializer


class Demos(APIView):
    def get(self, request):
        demos = Demo.objects.all()
        serializer = DemoSerializer(
            demos,
            many=True,
        )
        return Response(serializer.data)


class DemoAnimes(APIView):
    def get(self, request, demo_pk):
        anime_by_demo = DemoList.objects.all().filter(demo_id=demo_pk)
        serializer = DemoListSerializer(anime_by_demo, many=True)
        return Response(serializer.data)
