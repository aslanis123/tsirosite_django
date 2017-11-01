from django.db import models
from tinymce.models import HTMLField
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField




class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_descr = RichTextUploadingField()
    recipe_photo = models.ImageField(upload_to='images/', null=True, blank=True)

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_date = models.DateField()
    blog_descr = models.TextField()
    blog_author = models.ForeignKey('auth.User')
    blog_image = models.ImageField(upload_to='images/', null=True, blank=True)
    blog_text = RichTextUploadingField()

    def __str__(self):
        return self.blog_title
