from django import forms
from .models import Recipe, Blog

class PostForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('recipe_name', 'recipe_descr','recipe_photo')

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_date','blog_author','blog_descr','blog_text','blog_image')

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )

    #def __init__(self, *args, **kwargs):
    #    super(ContactForm, self).__init__(*args, **kwargs)
    #    self.fields['contact_name'].label = "Your name:"
    #    self.fields['contact_email'].label = "Your email:"
    #    self.fields['content'].label = "What do you want to say?"
