from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import LoginForm, PasswordResetForm
from .utils import staff_member_required


@staff_member_required
def index(request):
    ctx = {}
    return render(request, 'dashboard/index.html', ctx)


def login(request):
    kwargs = {
        'template_name': 'dashboard/login.html',
        'authentication_form': LoginForm
    }
    return auth_views.LoginView.as_view(**kwargs)(request, **kwargs)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


def password_reset(request):
    kwargs = {
        'template_name': 'dashboard/password_reset.html',
        'success_url': reverse_lazy('dashboard:password-reset-done'),
        'form_class': PasswordResetForm
    }
    return auth_views.PasswordResetView.as_view(**kwargs)(request, **kwargs)


def password_reset_done(request):
    kwargs = {
        'template_name': 'dashboard/password_reset_done.html',
    }
    return auth_views.PasswordResetView.as_view(**kwargs)(request, **kwargs)


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'dashboard/password_reset_from_key.html'
    success_url = reverse_lazy('dashboard:password-reset-complete')
    token = None
    uidb64 = None


def password_reset_confirm(request, uidb64=None, token=None):
    kwargs = {
        'template_name': 'dashboard/password_reset_from_key.html',
        'success_url': reverse_lazy('dashboard:password-reset-complete'),
        'token': token,
        'uidb64': uidb64
    }
    return PasswordResetConfirm.as_view(**kwargs)(request, **kwargs)


def password_reset_complete(request):
    kwargs = {
        'template_name': 'dashboard/password_reset_from_key_done.html'
    }
    return auth_views.PasswordResetCompleteView.as_view(**kwargs)(request, **kwargs)
