from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe, Plant
from .serializers import RecipeSerializer, PlantSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer
