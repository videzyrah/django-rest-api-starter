from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prep_time = models.IntegerField(help_text="in minutes")
    cook_time = models.IntegerField(help_text="in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Plant(models.Model):
    scientific_name = models.CharField(max_length=255)
    common_names =  models.CharField(max_length=255)
    edible_parts = models.CharField(max_length=255)
    minZone = models.IntegerField(help_text="minimum USDA zone 1-9")
    maxZone = models.IntegerField(help_text=" maximum USDA zone 1-9")
    soil_types = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


