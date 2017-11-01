"""tsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', app.views.landing, name='landing'),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^home$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^thanks/$', app.views.thanks, name='thanks'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^recipes$', app.views.recipes, name='recipes'),
    url(r'^admin/', admin.site.urls),
    url(r'^recipe/(?P<recipe_id>[0-9]+)/$', app.views.recipe_info_page, name='recipe_info_page'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', app.views.blog_info, name='blog_info'),
    url(r'^post/new/$', app.views.post_new, name='post_new'),
    url(r'^post/new/blog/$', app.views.post_new_blog, name='post_new_blog'),
    url(r'^(?P<recipe_id>[0-9]+)/edit/$', app.views.edit_existed, name='edit_existed'),
    url(r'^blog/(?P<blog_id>[0-9]+)/edit/$', app.views.edit_existed_blog, name='edit_existed_blog'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
