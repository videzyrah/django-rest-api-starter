from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    tools = models.CharField(max_length=255, default="Instapot")
    costs = models.CharField(max_length=255)
    procedure = models.TextField()
    notes = models.TextField()
    image_url = models.CharField(max_length = 200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Retailer(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    contact = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Plant(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    screen_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    common_names =  models.CharField(max_length=255)
    edible_parts = models.CharField(max_length=255)
    minZone = models.IntegerField(help_text="minimum USDA zone 1-9")
    maxZone = models.IntegerField(help_text=" maximum USDA zone 1-9")
    soil_types = models.CharField(
        max_length=255, 
        blank=True,
        help_text= "tolerates sand, tolerates clay, etc."
    )
    
    drought_tolerance_choices = (
        ('a', 'All'),
        ('h', 'High'),
        ('f', 'Moderate'),
        ('l', 'Low'),
    )

    drought_tolerance = models.CharField(
        max_length=1,
        choices= drought_tolerance_choices,
        blank=True,
        default='a',
        help_text='help text',
    )
    image = models.CharField(max_length = 200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    retailers= models.ManyToManyField(Retailer, blank=True)
    def __str__(self):
        return self.screen_name


