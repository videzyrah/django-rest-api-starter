from rest_framework import serializers
from .models import Recipe, Plant, Retailer

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url', 'name', 'ingredients', 'tools', 'costs', 'procedure', 'notes', 'image_url', 'created_at' )

class RetailerSerializer(serializers.RelatedField): 
    def to_representation(self, value):
         return "<a href= '%s'>%s</a>" % (value.link, value.name)
        
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
        fields = ('id', 'url', 'name', 'contact', 'link', 'notes')
