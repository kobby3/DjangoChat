from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Post, Comment
from .forms import *
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'chat/post_list.html', context)

def post_detail(request, id, slug):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=post, user=request.user, content=content)
            comment.save()
            
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'chat/post_detail.html', context)

def user_login(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    
    return render(request, 'chat/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('post_list')