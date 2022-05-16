from celery import shared_task
from django.conf import settings
from templated_email import send_templated_mail
from django.urls import reverse
from ..utils import build_absolute_uri, get_email_base_context


@shared_task
def send_password_reset_email(context, recipient):
    reset_url = build_absolute_uri(
        reverse(
            'dashboard:password-reset-confirm',
            kwargs={'uidb64': context['uid'], 'token': context['token']}
        )
    )
    context = get_email_base_context()
    context['reset_url'] = reset_url
    send_templated_mail(
        template_name='account/password_reset.email',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
        context=context
    )


@shared_task
def send_info_signin_email(email, password):
    context = get_email_base_context()
    login_url = build_absolute_uri(
        reverse('dashboard:login')
    )
    context['email'] = email
    context['password'] = password
    context['login_url'] = login_url
    send_templated_mail(
        template_name='account/info_signin.email',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        context=context
    )

