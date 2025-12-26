from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from assignments.models import About

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True, status = "published").order_by('created_at')
    posts = Blog.objects.filter(is_featured = False, status = "published")
    
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'categories' : categories,
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }
    return render(request, 'home.html', context)