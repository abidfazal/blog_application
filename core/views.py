from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Author,BlogPost 
from .forms import BlogForm,LoginForm,SignUpForm
from django.contrib.auth import logout

# Create your views here.

def home(request):
    blogs = BlogPost.objects.all()
    return render(request,'home_page.html',{'blogs':blogs})

def post_of_an_author(request,author):
    author_posts = BlogPost.objects.filter(author__name=author)
    return render(request,'author_posts.html',{'author_posts':author_posts})

def blog_details(request,pk):
    details = BlogPost.objects.get(pk=pk)
    return render(request,'details.html',{'blog':details})


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form is valid')
            # title = request.POST['title']
            # content = request.POST['content']
            # published = request.POST['publication_date']
            # author = request.POST['author']
            # BlogPost.objects.create(title=title, content=content, publication_date=published, author=author)
            return redirect('core:home')
    else:
        form = BlogForm()
    return render(request,'add_blog.html',{'form':form})
        
        
def sign_up(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def log_out(request):
    logout(request)
    
    return redirect('core:home')
    
    
