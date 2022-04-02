from django.urls import path, include
from .views import *


urlpatterns = [
    path('',PostViewSet.as_view(), name='post'),
    path('like/',PostLikesViewSet.as_view(), name='like'),
    path('story/',StoryViewSet.as_view(), name='story'),
    path('highlight/',HighlightViewSet.as_view(), name='highlight'),
    path('comments/',CommentViewSet.as_view(), name='comments')
]