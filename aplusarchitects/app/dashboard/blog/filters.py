import django_filters
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from ...blog.models import Post


class PostFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(label=pgettext_lazy(
        'Post filter label', 'ID'), field_name='id', lookup_expr='exact')
    title = django_filters.CharFilter(label=pgettext_lazy(
        'Post filter label', 'Title'), field_name='title', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = [
            'id', 'title',
        ]
