from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'prep_time', 'cook_time', 'created_at')
