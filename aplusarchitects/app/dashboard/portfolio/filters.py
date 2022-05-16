import django_filters
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from ...portfolio.models import Category, Project


class ProjectFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(
        label=pgettext_lazy('Project filter label', 'ID'),
        field_name='id',
        lookup_expr='exact'
    )
    name = django_filters.CharFilter(
        label=pgettext_lazy('Project filter label', 'Name'),
        field_name='name',
        lookup_expr='icontains'
    )
    category = django_filters.ModelChoiceFilter(
        label=pgettext_lazy('Project filter label', 'Category'),
        empty_label=pgettext_lazy('Project filter label', 'Select a category'),
        field_name='category',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'category']
