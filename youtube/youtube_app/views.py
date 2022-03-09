from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView

from .models import Mijoz,Playlist,Comment,Video
from .serializers import MijozSerializer,PlaylistSerializer,VideoSerializer,CommentSerializer


class MijizAPIView(ListCreateAPIView):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["ism"]

    def get_queryset(self):
        mijozs = Mijoz.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            mijozs = Mijoz.objects.annotate(
                similarity=TrigramSimilarity("ism", soz)
            ).filter(similarity__gte=0.4).order_by("-similarity")
        return mijozs

class MijozRUD(RetrieveUpdateDestroyAPIView):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer


class PlaylistAPIView(ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["nom"]

    def get_queryset(self):
        playlists = Playlist.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            playlists = Playlist.objects.annotate(
                similarity=TrigramSimilarity("nom", soz)
            ).filter(similarity__gte=0.4).order_by("-similarity")
        return playlists


class PlaylistRUD(RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class VideoAPIView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["nomi"]

    def get_queryset(self):
        videos = Video.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            videos = Video.objects.annotate(
                similarity=TrigramSimilarity("nomi", soz)
            ).filter(similarity__gte=0.4).order_by("-similarity")
        return videos

class VideoD(DestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CommentAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentD(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer