from rest_framework.serializers import ModelSerializer
from .models import Video,Comment,Playlist,Mijoz


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'
