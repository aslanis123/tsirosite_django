from django.shortcuts import render,get_object_or_404
from django.core.mail import BadHeaderError, send_mail
from datetime import datetime
from .models import Recipe, Blog
from .forms import PostForm, ContactForm
from django.shortcuts import redirect


def landing(request):
    return render(request, 'app/landing.html',{

        'title': 'Welcome to my Journey!',
    })

def home(request):
    return render(
        request,
        'app/home.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def about(request):
    return render(request, 'app/about.html',
        {
            'title':'About',
            'year':datetime.now().year,
        }
    )

def recipes(request):
    reps = Recipe.objects.all()
    return render(request, 'app/recipes.html',
        {
            'title':'My recipes',
            'recipes':reps,
        }
    )

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                send_mail(contact_name, content, contact_email,['dtzimoulidis@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('./thanks/')
    return render(request, 'app/contact.html', {'form': form})



def thanks(request):
    return render(request, 'app/thanks.html', {})


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'app/blog.html',
    {
        'blogs':blogs,
    })

def recipe_info_page(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'app/recipe_info_page.html',
        {
            'title':recipe.recipe_name,
            'image':recipe.recipe_photo.url,
            'desc':recipe.recipe_descr,
            'id':recipe.id,

        }
    )

def blog_info(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'app/blog_info.html',
        {
            'title':blog.blog_title,
            'desc':blog.blog_descr,
            'author':blog.blog_author,
            'date':blog.blog_date,
            'text':blog.blog_text,
            'id':blog.id,
        }
    )

def edit_existed(request,recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_info_page', recipe_id)
    else:
        form = PostForm(instance=recipe)

    return render(request, 'app/recipe_edit.html', {'form': form})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    else:
        form = PostForm()

    return render(request, 'app/recipe_edit.html', {'form': form})
