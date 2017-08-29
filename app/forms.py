from django import forms
from .models import Recipe

from .models import Recipe

class PostForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('recipe_name', 'recipe_descr','recipe_photo')
