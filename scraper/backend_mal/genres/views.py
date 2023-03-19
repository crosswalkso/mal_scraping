from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Genre
from .serializers import *
from animes.serializers import AnimeSerializer


class Genres(APIView):
    def get(self, request):
        all_genres = Genre.objects.all()
        serializer = GenreSerializer(
            all_genres,
            many=True,
        )
        return Response(serializer.data)


class GenreDetail(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


class GenreAnimes(APIView):
    def get_genre(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise NotFound

    def get(self, request, genre_pk):
        genre = self.get_genre(genre_pk).animegenres.values()[0]["anime_id"]
        print(genre)
        serializer = AnimeGenreSerializer(genre)
        return Response(serializer.data)
