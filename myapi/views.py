from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe, Plant, Retailer
from .serializers import RecipeSerializer, PlantSerializer, RetailerSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('name')
    serializer_class = RecipeSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('screen_name')
    serializer_class = PlantSerializer

class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all().order_by('id')
    serializer_class = RetailerSerializer
