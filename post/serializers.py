from rest_framework.serializers import ModelSerializer
from .models import *

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostLikesSerializer(ModelSerializer):
    class Meta:
        model = PostLikes
        fields = '__all__'

class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'

class HighlightSerializer(ModelSerializer):
    class Meta:
        model = Highlight
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentLikeSerializer(ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'