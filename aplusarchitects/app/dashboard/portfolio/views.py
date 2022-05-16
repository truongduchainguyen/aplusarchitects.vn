from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.utils.translation import gettext_lazy as _
from .forms import (
    CategoryForm, CategoryTranslationForm,
    ProjectForm, ProjectTranslationForm,
    ProjectImageForm, ProjectImageReorderForm
)
from .filters import ProjectFilter
from ..utils import get_paginator_items, staff_member_required
from ...portfolio.models import (
    Category, CategoryTranslation,
    Project, ProjectTranslation,
    ProjectImage
)


# Manage Category
@staff_member_required
@permission_required('portfolio.manage_category')
def category_list(request):
    categories = Category.objects.all().order_by('-id')
    categories = get_paginator_items(
        categories,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'categories': categories}
    return render(request, 'dashboard/portfolio/category/list.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_category')
def category_add(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        category = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:portfolio:category-change', pk=category.pk)
    ctx = {'form': form}
    return render(request, 'dashboard/portfolio/category/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_category')
def category_change(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        category = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:portfolio:category-change', pk=category.pk)
    ctx = {'category': category, 'form': form}
    return render(request, 'dashboard/portfolio/category/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_category')
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:portfolio:category-list')
    ctx = {'category': category}
    return render(request, 'dashboard/portfolio/category/modal/confirm_delete.html', ctx)


# Manage Category Translation
@staff_member_required
@permission_required('portfolio.manage_category')
def category_translate_add(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    translate = CategoryTranslation(category=category)
    form = CategoryTranslationForm(request.POST or None, instance=translate)
    if form.is_valid():
        translate = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:portfolio:category-translate-change', category_pk=category.pk, pk=translate.pk)
    ctx = {'form': form, 'category': category}
    return render(request, 'dashboard/portfolio/category_translate/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_category')
def category_translate_change(request, category_pk, pk):
    category = get_object_or_404(Category, pk=category_pk)
    translate = get_object_or_404(category.translations.all(), pk=pk)
    form = CategoryTranslationForm(request.POST or None, instance=translate)
    if form.is_valid():
        form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:portfolio:category-translate-change', category_pk=category.pk, pk=translate.pk)
    ctx = {'form': form, 'category': category, 'translate': translate}
    return render(request, 'dashboard/portfolio/category_translate/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_category')
def category_translate_delete(request, category_pk, pk):
    category = get_object_or_404(Category, pk=category_pk)
    translate = get_object_or_404(category.translations.all(), pk=pk)
    if request.method == 'POST':
        translate.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:portfolio:category-change', pk=category.pk)
    ctx = {'category': category, 'translate': translate}
    return render(request, 'dashboard/portfolio/category_translate/modal/confirm_delete.html', ctx)


# Manage Project
@staff_member_required
@permission_required('portfolio.manage_project')
def project_list(request):
    projects = Project.objects.all().order_by('-id')
    project_filter = ProjectFilter(request.GET, queryset=projects)
    projects = get_paginator_items(
        project_filter.qs,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'projects': projects, 'filter': project_filter}
    return render(request, 'dashboard/portfolio/project/list.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_add(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:portfolio:project-change', pk=project.pk)
    ctx = {'form': form}
    return render(request, 'dashboard/portfolio/project/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_change(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        project = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:portfolio:project-change', pk=project.pk)
    ctx = {'project': project, 'form': form}
    return render(request, 'dashboard/portfolio/project/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:portfolio:project-list')
    ctx = {'project': project}
    return render(request, 'dashboard/portfolio/project/modal/confirm_delete.html', ctx)


# Manage Project Translation
@staff_member_required
@permission_required('portfolio.manage_project')
def project_translate_add(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    translate = ProjectTranslation(project=project)
    form = ProjectTranslationForm(request.POST or None, instance=translate)
    if form.is_valid():
        translate = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:portfolio:project-translate-change', project_pk=project.pk, pk=translate.pk)
    ctx = {'form': form, 'project': project}
    return render(request, 'dashboard/portfolio/project_translate/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_translate_change(request, project_pk, pk):
    project = get_object_or_404(Project, pk=project_pk)
    translate = get_object_or_404(project.translations.all(), pk=pk)
    form = ProjectTranslationForm(request.POST or None, instance=translate)
    if form.is_valid():
        form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:portfolio:project-translate-change', project_pk=project.pk, pk=translate.pk)
    ctx = {'form': form, 'project': project, 'translate': translate}
    return render(request, 'dashboard/portfolio/project_translate/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_translate_delete(request, project_pk, pk):
    project = get_object_or_404(Project, pk=project_pk)
    translate = get_object_or_404(project.translations.all(), pk=pk)
    if request.method == 'POST':
        translate.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:portfolio:project-change', pk=project.pk)
    ctx = {'project': project, 'translate': translate}
    return render(request, 'dashboard/portfolio/project_translate/modal/confirm_delete.html', ctx)


# Manage Project Image
@staff_member_required
@permission_required('portfolio.manage_project')
def project_images(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    images = project.images.all()
    ctx = {'project': project, 'images': images}
    return render(request, 'dashboard/portfolio/project_image/list.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_images_add(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    project_image = ProjectImage(project=project)
    form = ProjectImageForm(request.POST or None, request.FILES or None, instance=project_image)
    if form.is_valid():
        form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:portfolio:project-images-list', project_pk=project.pk)
    ctx = {'project': project, 'form': form}
    return render(request, 'dashboard/portfolio/project_image/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_images_change(request, project_pk, pk):
    project = get_object_or_404(Project, pk=project_pk)
    project_image = get_object_or_404(project.images.all(), pk=pk)
    form = ProjectImageForm(request.POST or None, request.FILES or None, instance=project_image)
    if form.is_valid():
        form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:portfolio:project-images-list', project_pk=project.pk)
    ctx = {'form': form, 'project': project, 'project_image': project_image}
    return render(request, 'dashboard/portfolio/project_image/form.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_images_delete(request, project_pk, pk):
    project = get_object_or_404(Project, pk=project_pk)
    project_image = get_object_or_404(project.images.all(), pk=pk)
    if request.method == 'POST':
        project_image.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:portfolio:project-images-list', project_pk=project.pk)
    ctx = {'project': project, 'project_image': project_image}
    return render(request, 'dashboard/portfolio/project_image/modal/confirm_delete.html', ctx)


@staff_member_required
@permission_required('portfolio.manage_project')
def project_images_reorder(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    status = 200
    ctx = {}
    if request.method == 'POST':
        form = ProjectImageReorderForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
        elif form.errors:
            status = 400
            ctx = {'message': form.errors}
    return JsonResponse(ctx, status=status)
