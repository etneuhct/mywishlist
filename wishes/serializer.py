from rest_framework import serializers
from wishes.models import Wish
from wishes.models import Friend


class WishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wish
        fields = ['id', 'name', 'friend']


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = ['id', 'first_name', 'last_name']

