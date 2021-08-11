from rest_framework import serializers
from .models import Recipe, Plant, Retailer

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url', 'name', 'ingredients', 'tools', 'costs', 'procedure', 'notes', 'created_at')

class RetailerSerializer(serializers.HyperlinkedModelSerializer):
    
    def to_representation(self, value):
         return '%s: %s' % (value.name, value.contact)

    class Meta:
        model = Retailer
        fields = ('id', 'url', 'contact', 'name', 'link', 'notes')
        
class PlantSerializer(serializers.HyperlinkedModelSerializer):
    retailers = RetailerSerializer(read_only=True, many=True)
 
    class Meta:
        model = Plant
        fields = ('id', 
                  'url',
                  'screen_name',
                  'scientific_name', 
                  'common_names', 
                  'edible_parts', 
                  'minZone', 'maxZone', 
                  'soil_types', 
                  'drought_tolerance',
                  'created_at',
                  'image',
                  'price',
                  'retailers',
                  )

class GrowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Retailer
        fields = ('id', 'url', 'contact', 'name', 'plant_list', 'link', 'notes')
