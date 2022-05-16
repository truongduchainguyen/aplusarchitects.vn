from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.utils.translation import gettext_lazy as _
from .forms import ServiceForm, ServiceTranslationForm
from ..utils import get_paginator_items, staff_member_required
from ...service.models import Service, ServiceTranslation


@staff_member_required
@permission_required('service.manage_service')
def service_list(request):
    services = Service.objects.all().order_by('-id')
    services = get_paginator_items(
        services,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'services': services}
    return render(request, 'dashboard/service/list.html', ctx)


@staff_member_required
@permission_required('service.manage_service')
def service_add(request):
    form = ServiceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        service = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:service:service-change', pk=service.pk)
    ctx = {'form': form}
    return render(request, 'dashboard/service/form.html', ctx)


@staff_member_required
@permission_required('service.manage_service')
def service_change(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None,
                       request.FILES or None, instance=service)
    if form.is_valid():
        service = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:service:service-change', pk=service.pk)
    ctx = {'service': service, 'form': form}
    return render(request, 'dashboard/service/form.html', ctx)


@staff_member_required
@permission_required('service.manage_service')
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:service:service-list')
    ctx = {'service': service}
    return render(request, 'dashboard/service/modal/confirm_delete.html', ctx)


@staff_member_required
@permission_required('service.manage_service')
def service_translate_add(request, service_pk):
    service = get_object_or_404(Service, pk=service_pk)
    translate = ServiceTranslation(service=service)
    form = ServiceTranslationForm(request.POST or None, instance=translate)
    if form.is_valid():
        translate = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:service:service-change', pk=service.pk)
    ctx = {'form': form, 'service': service}
    return render(request, 'dashboard/service/translate_form.html', ctx)


@staff_member_required
@permission_required('service.manage_service')
def service_translate_change(request, service_pk, pk):
    service = get_object_or_404(Service, pk=service_pk)
    translate = get_object_or_404(service.translations.all(), pk=pk)
    form = ServiceTranslationForm(request.POST or None, instance=translate)
    if form.is_valid():
        form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:service:service-translate-change', service_pk=service.pk, pk=translate.pk)
    ctx = {'form': form, 'service': service, 'translate': translate}
    return render(request, 'dashboard/service/translate_form.html', ctx)


@staff_member_required
@permission_required('service.manage_service')
def service_translate_delete(request, service_pk, pk):
    service = get_object_or_404(Service, pk=service_pk)
    translate = get_object_or_404(service.translations.all(), pk=pk)
    if request.method == 'POST':
        translate.delete()
        messages.success(request, _('Removed successfully.'))
        return redirect('dashboard:service:service-change', pk=service.pk)
    ctx = {'service': service, 'translate': translate}
    return render(request, 'dashboard/service/modal/translate_confirm_delete.html', ctx)
