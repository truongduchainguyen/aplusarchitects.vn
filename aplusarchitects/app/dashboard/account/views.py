from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileForm, PasswordChangeForm, CustomerForm, StaffForm
from .filters import CustomerFilter, StaffFilter
from ..utils import staff_member_required, get_paginator_items
from ...account.models import User
from ...account.emails import send_info_signin_email


@login_required
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, _('Updated your profile.'))
        return redirect('dashboard:account:profile')
    ctx = {'form': form}
    return render(request, 'dashboard/account/profile.html', ctx)


@login_required
def password_change(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        messages.success(request, _('Updated your password.'))
        return redirect('dashboard:account:password-change')
    ctx = {'form': form}
    return render(request, 'dashboard/account/password_change.html', ctx)


# Customer
@staff_member_required
@permission_required('account.manage_customer')
def customer_list(request):
    customers = User.objects.filter(is_staff=False).order_by('-id')
    customer_filter = CustomerFilter(request.GET, queryset=customers)
    customers = get_paginator_items(
        customer_filter.qs,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'customers': customers, 'filter': customer_filter}
    return render(request, 'dashboard/account/customer/list.html', ctx)


@staff_member_required
@permission_required('account.manage_customer')
def customer_add(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        customer = form.save()
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:account:customer-change', pk=customer.pk)
    ctx = {'form': form}
    return render(request, 'dashboard/account/customer/form.html', ctx)


@staff_member_required
@permission_required('account.manage_customer')
def customer_delete(request, pk):
    customers = User.objects.filter(is_staff=False)
    customer = get_object_or_404(customers, pk=pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, _('%s successfully removed.') % customer)
        return redirect('dashboard:account:customer-list')
    ctx = {'customer': customer}
    return render(request, 'dashboard/account/customer/modal/confirm_delete.html', ctx)


@staff_member_required
@permission_required('account.manage_customer')
def customer_change(request, pk):
    customers = User.objects.filter(is_staff=False)
    customer = get_object_or_404(customers, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        customer = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:account:customer-change', pk=customer.pk)
    ctx = {'customer': customer, 'form': form}
    return render(request, 'dashboard/account/customer/form.html', ctx)


# Staff
@staff_member_required
@permission_required('account.manage_staff')
def staff_list(request):
    staffs = User.objects.filter(is_staff=True).order_by('-id')
    staff_filter = StaffFilter(request.GET, queryset=staffs)
    staffs = get_paginator_items(
        staff_filter.qs,
        settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page')
    )
    ctx = {'staffs': staffs, 'filter': staff_filter}
    return render(request, 'dashboard/account/staff/list.html', ctx)


@staff_member_required
@permission_required('account.manage_staff')
def staff_add(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        staff = form.save(commit=False)
        staff.is_staff = True
        _password = User.objects.make_random_password()
        staff.set_password(_password)
        staff.save()
        send_info_signin_email.delay(staff.email, _password)
        messages.success(request, _('Added successfully.'))
        return redirect('dashboard:account:staff-change', pk=staff.pk)
    ctx = {'form': form}
    return render(request, 'dashboard/account/staff/form.html', ctx)


@staff_member_required
@permission_required('account.manage_staff')
def staff_delete(request, pk):
    staffs = User.objects.filter(is_staff=True)
    staff = get_object_or_404(staffs, pk=pk)
    if request.method == 'POST':
        staff.delete()
        messages.success(request, _('%s successfully removed.') % staff)
        return redirect('dashboard:account:staff-list')
    ctx = {'staff': staff}
    return render(request, 'dashboard/account/staff/modal/confirm_delete.html', ctx)


@staff_member_required
@permission_required('account.manage_staff')
def staff_change(request, pk):
    staffs = User.objects.filter(is_staff=True)
    staff = get_object_or_404(staffs, pk=pk)
    form = StaffForm(request.POST or None, instance=staff)
    if form.is_valid():
        staff = form.save()
        messages.success(request, _('Updated successfully.'))
        return redirect('dashboard:account:staff-change', pk=staff.pk)
    ctx = {'staff': staff, 'form': form}
    return render(request, 'dashboard/account/staff/form.html', ctx)
