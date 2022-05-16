from django.shortcuts import render, get_object_or_404
from .models import Category, Project


def index(request):
    categories = Category.objects.all().order_by('-id')
    projects = Project.objects.all().order_by('-id')
    ctx = {'categories': categories, 'projects': projects}
    return render(request, 'portfolio/index.html', ctx)


def detail(request, slug, pk):
    project = get_object_or_404(Project, pk=pk)
    ctx = {'project': project}
    return render(request, 'portfolio/detail.html', ctx)
