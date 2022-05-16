from django import forms
from django.utils.translation import gettext_lazy as _
from ...blog.models import Category, Tag, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = []


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        labels = {
            'category': _('Category'),
            'tag': _('Tag'),
            'image': _('Image'),
        }
        help_texts = {
            'image': _('Image size 1240 × 800.'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        select2_no_search = {
            'data-plugin': 'select2',
            'data-minimum-results-for-search': 'Infinity',
            'data-placeholder': _('Select an option')
        }
        self.fields['category'].widget.attrs.update(select2_no_search)
        self.fields['tag'].widget.attrs.update({'data-plugin': 'select2'})
