from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieDBViewSet, GenreDBViewSet

router = DefaultRouter()
router.register('movies', MovieDBViewSet, basename='movies')
router.register('genres', GenreDBViewSet, basename='genres')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls 