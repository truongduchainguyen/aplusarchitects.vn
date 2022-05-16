from django import forms
from ...service.models import Service, ServiceTranslation


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'background', 'percent', 'sort_order']


class ServiceTranslationForm(forms.ModelForm):
    class Meta:
        model = ServiceTranslation
        fields = ['language_code', 'service', 'name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].widget = forms.HiddenInput()


