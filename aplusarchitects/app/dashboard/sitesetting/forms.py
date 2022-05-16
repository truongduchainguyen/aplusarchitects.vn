from django import forms
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from ...sitesetting.models import SiteSettings, SocialNetwork


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        exclude = []
        labels = {
            'domain': _('Domain'),
            'name': _('Site name')
        }


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        exclude = ['site']


class SocialNetworkForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        exclude = []
