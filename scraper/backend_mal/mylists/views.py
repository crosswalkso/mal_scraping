from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from animes.models import Anime
from .models import Mylist
from .serializers import MylistSerializer, MylistDetailSerializer

# Create your views here.


class Mylists(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_mylists = Mylist.objects.filter(user=request.user)
        serializer = MylistSerializer(
            all_mylists,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = MylistSerializer(data=request.data)
        if serializer.is_valid():
            mylist = serializer.save(user=request.user)
            serializer = MylistSerializer(mylist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MylistDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):  # private - user도 전달!
        try:
            return Mylist.objects.get(
                pk=pk,
                user=user,
            )
        except Mylist.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        mylist = self.get_object(pk, request.user)
        serializer = MylistDetailSerializer(mylist)
        return Response(serializer.data)

    def delete(self, request, pk):
        mylist = self.get_object(pk, request.user)
        mylist.delete()
        return Response(status=HTTP_200_OK)

    def put(self, request, pk):
        mylist = self.get_object(pk, request.user)
        serializer = MylistDetailSerializer(
            mylist,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            mylist = serializer.save()
            serializer = MylistDetailSerializer(mylist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MylistToggle(APIView):
    def get_list(self, pk, user):
        try:
            return Mylist.objects.get(
                pk=pk,
                user=user,
            )
        except Mylist.DoesNotExist:
            raise NotFound

    def get_anime(self, pk):
        try:
            return Anime.objects.get(pk=pk)
        except Anime.DoesNotExist:
            raise NotFound

    def put(self, request, pk, anime_pk):
        mylist = self.get_list(pk, request.user)
        anime = self.get_anime(anime_pk)

        if mylist.animes.filter(pk=anime.pk).exists():
            mylist.animes.remove(anime)
        else:
            mylist.animes.add(anime)
        return Response(status=HTTP_200_OK)
