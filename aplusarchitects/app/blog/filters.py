import django_filters
from django.utils.translation import pgettext_lazy
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label=pgettext_lazy(
        'Post filter label', 'Title'), field_name='title', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title']
