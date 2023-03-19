from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *


class Broadcasts(APIView):
    def get(self, request):
        all_broadcasts = Broadcast.objects.all()
        serializer = BroadcastSerializer(
            all_broadcasts,
            many=True,
        )
        return Response(serializer.data)


class BroadcastDetail(APIView):
    def get_object(self, pk):
        try:
            return Broadcast.objects.get(pk=pk)
        except Broadcast.DoesNotExist:
            raise NotFound

    def get(self, request, broad_pk):
        broadcast = self.get_object(broad_pk)
        serializer = BroadcastSerializer(broadcast)
        return Response(serializer.data)


class BroadcastList(APIView):
    def get_object(self, pk):
        try:
            return Broadcast.objects.get(pk=pk)
        except Broadcast.DoesNotExist:
            raise NotFound

    def get(self, request, broad_pk):
        broadcast = self.get_object(broad_pk)
        animes = broadcast.broadcastlist_set.all()
        serializer = BroadcastListSerializer(animes)
        return Response(serializer.data)
