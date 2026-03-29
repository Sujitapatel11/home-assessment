from rest_framework import serializers
from .models import Favourite
from properties.serializers import PropertySerializer


class FavouriteSerializer(serializers.ModelSerializer):
    property_detail = PropertySerializer(source='property', read_only=True)

    class Meta:
        model = Favourite
        fields = ('id', 'property', 'property_detail', 'created_at')
        extra_kwargs = {'property': {'write_only': True}}
