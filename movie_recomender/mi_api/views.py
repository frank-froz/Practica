from rest_framework import viewsets
from .models import MovieDB, GenreDB
from .serializers import MovieDBSerializer, GenreDBSerializer
# Create your views here.

class MovieDBViewSet(viewsets.ModelViewSet):
    queryset = MovieDB.objects.all()
    serializer_class = MovieDBSerializer

class GenreDBViewSet(viewsets.ModelViewSet):
    queryset = GenreDB.objects.all()
    serializer_class = GenreDBSerializer