from rest_framework import serializers
from blocitoff.models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        fields = ('url', 'id', 'name', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(many=True, view_name='item', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'items')
