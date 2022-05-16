from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from ..account.models import User
from ..account.emails import send_password_reset_email


class LoginForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(label=_('Email'), max_length=255)
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        if request:
            email = request.GET.get('email')
            if email:
                self.fields['username'].initial = email


class PasswordResetForm(auth_forms.PasswordResetForm):
    def get_users(self, email):
        active_users = User.objects.filter(email__iexact=email, is_active=True)
        return active_users

    def send_mail(
            self, subject_template_name, email_template_name, context,
            from_email, to_email, html_email_template_name=None):
        del context['user']
        send_password_reset_email.delay(context, to_email)
