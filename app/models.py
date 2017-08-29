from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_descr = models.TextField()
    recipe_photo = models.ImageField(upload_to='images/', null=True, blank=True)
