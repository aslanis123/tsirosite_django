from django.db import models
from tinymce.models import HTMLField


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_descr = HTMLField()
    recipe_photo = models.ImageField(upload_to='images/', null=True, blank=True)
