from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from ...account.models import User
from ..permissions import get_permissions


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        label=_('Date of birth'),
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
        required=True,
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({
            'data-plugin': 'datepicker',
            'data-format': 'dd/mm/yyyy'
        })
        self.fields['email'].disabled = True


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomerForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        label=_('Date of birth'),
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
        required=True,
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({
            'data-plugin': 'datepicker',
            'data-format': 'dd/mm/yyyy'
        })


class PermissionMultipleChoiceField(forms.ModelMultipleChoiceField):
    """ Permission multiple choice field with label override."""

    def label_from_instance(self, obj):
        return obj.name


class StaffForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        label=_('Date of birth'),
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
        required=True,
    )

    user_permissions = PermissionMultipleChoiceField(
        label=_('Permissions'),
        queryset=get_permissions(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name',
            'date_of_birth', 'user_permissions',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({
            'data-plugin': 'datepicker',
            'data-format': 'dd/mm/yyyy'
        })
