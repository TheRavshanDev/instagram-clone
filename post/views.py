from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

class PostViewSet(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostLikesViewSet(ListCreateAPIView, RetrieveUpdateAPIView):
    queryset = PostLikes.objects.all()
    serializer_class = PostLikesSerializer

class StoryViewSet(ListCreateAPIView, DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class HighlightViewSet(ListCreateAPIView, DestroyAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer

class CommentViewSet(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer