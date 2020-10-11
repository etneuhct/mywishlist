from django.shortcuts import render
from rest_framework import viewsets
from wishes.models import Friend, Wish
from wishes.serializer import FriendSerializer, WishSerializer


class FriendViewSet(viewsets.ModelViewSet):
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()


class WishViewSet(viewsets.ModelViewSet):
    serializer_class = WishSerializer
    queryset = Wish.objects.all()
