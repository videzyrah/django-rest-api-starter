from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prep_time = models.IntegerField(help_text="in minutes")
    cook_time = models.IntegerField(help_text="in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
