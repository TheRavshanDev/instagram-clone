from django.urls import path, include
from .views import AccountViewSet


urlpatterns = [
    path('',AccountViewSet.as_view(), name='account'),
]