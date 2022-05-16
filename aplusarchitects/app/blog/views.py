from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .filters import PostFilter
from ..utils import get_paginator_items


def index(request):
    posts = Post.objects.all().order_by('-id')

    last_posts = posts.order_by('-created_at')[:4]
    tags = None
    categories = Category.objects.all().order_by('-id')

    post_filter = PostFilter(request.GET, queryset=posts)
    posts = get_paginator_items(
        post_filter.qs,
        5,
        request.GET.get('page')
    )

    ctx = {
        'posts': posts,
        'filter': post_filter,
        'last_posts': last_posts,
        'categories': categories,
    }
    return render(request, 'blog/index.html', ctx)


def detail(request, slug, pk):
    post = get_object_or_404(Post, pk=pk)
    related_posts = Post.objects.filter(category=post.category).exclude(
        pk=post.pk).order_by('-created_at')[:4]
    categories = Category.objects.all().order_by('-id')
    ctx = {
        'post': post,
        'related_posts': related_posts,
        'categories': categories
    }
    return render(request, 'blog/detail.html', ctx)


def category(request, slug, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-id')
    posts = get_paginator_items(
        posts,
        5,
        request.GET.get('page')
    )
    ctx = {'category': category, 'posts': posts}
    return render(request, 'blog/category.html', ctx)
