from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.utils.translation import gettext_lazy as _
from ...blog.models import Category, Tag, Post
from ..utils import get_paginator_items, staff_member_required
from .forms import CategoryForm, TagForm, PostForm
from .filters import PostFilter


@staff_member_required
@permission_required('blog.manage_category')
def category_list(request):
    categories = Category.objects.all().order_by('-id')
    categories = get_paginator_items(
        categories,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'categories': categories}
    return render(request, 'dashboard/blog/category/list.html', ctx)


@staff_member_required
@permission_required('blog.manage_category')
def category_add(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        category = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:blog:category-change', pk=category.pk)
    ctx = {'form': form}
    return render(request, 'dashboard/blog/category/form.html', ctx)


@staff_member_required
@permission_required('blog.manage_category')
def category_change(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        category = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:blog:category-change', pk=category.pk)
    ctx = {'category': category, 'form': form}
    return render(request, 'dashboard/blog/category/form.html', ctx)


@staff_member_required
@permission_required('blog.manage_category')
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:blog:category-list')
    ctx = {'category': category}
    return render(request, 'dashboard/blog/category/modal/confirm_delete.html', ctx)


@staff_member_required
@permission_required('blog.manage_tag')
def tag_list(request):
    tags = Tag.objects.all().order_by('-id')
    tags = get_paginator_items(
        tags,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'tags': tags}
    return render(request, 'dashboard/blog/tag/list.html', ctx)


@staff_member_required
@permission_required('blog.manage_tag')
def tag_add(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        tag = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:blog:tag-change', pk=tag.pk)
    ctx = {'form': form}
    return render(request, 'dashboard/blog/tag/form.html', ctx)


@staff_member_required
@permission_required('blog.manage_tag')
def tag_change(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagForm(request.POST or None, instance=tag)
    if form.is_valid():
        tag = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:blog:tag-change', pk=tag.pk)
    ctx = {'tag': tag, 'form': form}
    return render(request, 'dashboard/blog/tag/form.html', ctx)


@staff_member_required
@permission_required('blog.manage_tag')
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:blog:tag-list')
    ctx = {'tag': tag}
    return render(request, 'dashboard/blog/tag/modal/confirm_delete.html', ctx)


@staff_member_required
@permission_required('blog.manage_post')
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    post_filter = PostFilter(request.GET, queryset=posts)
    posts = get_paginator_items(
        post_filter.qs,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'posts': posts, 'filter': post_filter}
    return render(request, 'dashboard/blog/post/list.html', ctx)


@staff_member_required
@permission_required('blog.manage_post')
def post_add(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()

        for tag in form.cleaned_data['tag']:
            post.tag.add(tag)

        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:blog:post-change', pk=post.pk)
    ctx = {'form': form}
    return render(request, 'dashboard/blog/post/form.html', ctx)


@staff_member_required
@permission_required('blog.manage_post')
def post_change(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:blog:post-change', pk=post.pk)
    ctx = {'post': post, 'form': form}
    return render(request, 'dashboard/blog/post/form.html', ctx)


@staff_member_required
@permission_required('blog.manage_post')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:blog:post-list')
    ctx = {'post': post}
    return render(request, 'dashboard/blog/post/modal/confirm_delete.html', ctx)
