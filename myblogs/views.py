from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Category, Blog, Comment
from django.contrib.auth.models import User
from .import auth_views
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginUser')
def index(request):
    category = Category.objects.filter(user=request.user)
    query = request.GET.get('query', '')

    if query:
        blogs = Blog.objects.filter(user=request.user, title__icontains=query)
    else:
        blogs = Blog.objects.filter(user=request.user)

    return render(request, 'index.html', {'category': category, 'blogs': blogs})

@login_required(login_url='loginUser')
def writeBlog(request):
    user = request.user
    categories = user.category_set.all()
    # categories = Category.objects.all()
    # blogs = Blog.objects.get()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category = Category.objects.get_or_create(name=data['new_category'], user=user)
        else:
            category = None

        #retrieve the Category instance first and then assign it to the Photo object. 
        if isinstance(category, tuple):
            category = category[0]

        blogs = Blog.objects.create(
            category=category,
            title = data['title'],
            image=image,
            description=data['description'],
            user=user
        )     

        return redirect('index')
    
    return render(request, 'writeBlog.html', {'categories': categories})

@login_required(login_url='loginUser')
def yourBlog(request, pk):
    blogs = get_object_or_404(Blog, id=pk)
    comments = blogs.comment_set.all()

    if request.user == User:
        blogs = Blog.objects.get(id = pk, user=request.user)
    else:
        blogs = Blog.objects.get(id=pk)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text', '')

        if comment_text:
            Comment.objects.create(
                user=request.user,
                comment = comment_text,
                blog=blogs,
                created_by=request.user.username,
            )    
    return render(request, 'yourBlog.html', {'blogs': blogs, 'comments': comments})

@login_required(login_url='loginUser')
def editBlog(request, pk):
    blogs = Blog.objects.get(id = pk, user=request.user)

    if request.method == 'POST':
        blog_desc = request.POST.get('blog_desc', '')
        blogs.description = blog_desc
        blogs.save()

        return redirect('yourBlog', pk=pk)
    
    return render(request, 'editBlog.html', {'blogs': blogs})

@login_required(login_url='loginUser')
def deleteBlog(request, pk):
    blogs = get_object_or_404(Blog, id = pk, user=request.user)
    blogs.delete()
    return redirect('index')

@login_required(login_url='loginUser')
def blogfeed(request):
    blogs = Blog.objects.exclude(user=request.user)
    return render(request, 'blogfeed.html', {'blogs': blogs})
