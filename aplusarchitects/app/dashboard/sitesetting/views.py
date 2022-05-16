from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext_lazy as _
from ...sitesetting.models import SiteSettings, SocialNetwork
from .forms import SiteForm, SiteSettingsForm, SocialNetworkForm
from ..utils import staff_member_required, get_paginator_items


@staff_member_required
@permission_required('sitesetting.manage_sitesettings')
def index(request):
    ctx = {}
    return render(request, 'dashboard/sitesetting/index.html', ctx)


@staff_member_required
@permission_required('sitesetting.manage_sitesettings')
def general_information(request):
    site = get_current_site(request)

    try:
        site_setting = SiteSettings.objects.get(site=site)
    except:
        site_setting = SiteSettings()

    site_form = SiteForm(request.POST or None, instance=site)
    site_settings_form = SiteSettingsForm(
        request.POST or None, instance=site_setting)

    if site_form.is_valid() and site_settings_form.is_valid():
        site = site_form.save()
        site_settings = site_settings_form.save(commit=False)
        site_settings.site = site
        site_settings.save()
        messages.success(request, _('Updated site settings'))
        return redirect('dashboard:sitesetting:general-information')

    ctx = {
        'site_form': site_form,
        'site_settings_form': site_settings_form
    }
    return render(request, 'dashboard/sitesetting/general/form.html', ctx)


@staff_member_required
@permission_required('sitesetting.manage_sitesettings')
def social_network_list(request):
    social_list = SocialNetwork.objects.all().order_by('-id')
    social_list = get_paginator_items(
        social_list,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'social_list': social_list}
    return render(request, 'dashboard/sitesetting/social_network/list.html', ctx)


@staff_member_required
@permission_required('sitesetting.manage_sitesettings')
def social_network_add(request):
    form = SocialNetworkForm(request.POST or None)
    if form.is_valid():
        social = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:sitesetting:social-network-list')
    ctx = {'form': form}
    return render(request, 'dashboard/sitesetting/social_network/form.html', ctx)


@staff_member_required
@permission_required('sitesetting.manage_sitesettings')
def social_network_change(request, pk):
    social = get_object_or_404(SocialNetwork, pk=pk)
    form = SocialNetworkForm(request.POST or None, instance=social)
    if form.is_valid():
        social = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:sitesetting:social-network-change', pk=social.pk)
    ctx = {'social': social, 'form': form}
    return render(request, 'dashboard/sitesetting/social_network/form.html', ctx)


@staff_member_required
@permission_required('sitesetting.manage_sitesettings')
def social_network_delete(request, pk):
    social = get_object_or_404(SocialNetwork, pk=pk)
    if request.method == 'POST':
        social.delete()
        messages.success(request, _('%s successfully removed.') % social)
        return redirect('dashboard:sitesetting:social-network-list')
    ctx = {'social': social}
    return render(request, 'dashboard/sitesetting/social_network/modal/confirm_delete.html', ctx)
