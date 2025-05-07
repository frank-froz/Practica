from rest_framework import serializers
from mi_api.models import MovieDB, GenreDB

class MovieDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDB
        fields = '__all__'  


class GenreDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreDB
        fields = '__all__'  
