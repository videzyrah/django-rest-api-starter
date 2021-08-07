from rest_framework import serializers
from .models import Recipe, Plant

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url', 'name', 'ingredients', 'tools', 'costs', 'procedure', 'notes', 'created_at')

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'url', 'scientific_name', 'common_names', 'edible_parts', 'minZone', 'maxZone', 'soil_types', 'created_at')
