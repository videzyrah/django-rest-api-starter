from django.contrib import admin

# Register your models here.
from .models import Recipe, Plant

admin.site.register(Recipe)
admin.site.register(Plant)
