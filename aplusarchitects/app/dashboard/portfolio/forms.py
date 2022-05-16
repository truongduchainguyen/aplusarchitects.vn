from django import forms
from django.utils.translation import gettext_lazy as _
from ...portfolio.models import (
    Category, CategoryTranslation,
    Project, ProjectTranslation,
    ProjectImage
)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class CategoryTranslationForm(forms.ModelForm):
    class Meta:
        model = CategoryTranslation
        fields = ['language_code', 'category', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = forms.HiddenInput()


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'category', 'description', 'is_featured']
        labels = {
            'category': _('Category'),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        select2_no_search = {
            'data-plugin': 'select2',
            'data-minimum-results-for-search': 'Infinity',
            'data-placeholder': _('Select an option')
        }
        self.fields['category'].widget.attrs.update(select2_no_search)


class ProjectTranslationForm(forms.ModelForm):
    class Meta:
        model = ProjectTranslation
        fields = ['language_code', 'project', 'name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].widget = forms.HiddenInput()


class ProjectImageForm(forms.ModelForm):

    class Meta:
        model = ProjectImage
        fields = ['project', 'image', 'alt']
        labels = {
            'image': _('Image'),
            'alt': _('Alt'),
        }
        # help_texts = {
        #     'image': _('Image size is 1000 x 670px.'),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].widget = forms.HiddenInput()


class OrderedModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def clean(self, value):
        qs = super().clean(value)
        keys = list(map(int, value))
        return sorted(qs, key=lambda v: keys.index(v.pk))


class ProjectImageReorderForm(forms.ModelForm):
    ordered_images = OrderedModelMultipleChoiceField(
        queryset=ProjectImage.objects.none()
    )

    class Meta:
        model = Project
        fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['ordered_images'].queryset = self.instance.images.all()

    def save(self):
        for order, image in enumerate(self.cleaned_data['ordered_images']):
            image.sort_order = order
            image.save()
        return self.instance
