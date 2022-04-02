from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from .models import *
from .serializers import *

class AccountViewSet(ListCreateAPIView, UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer