from django.db.models import Q
import django_filters
from django.utils.translation import gettext_lazy as _
from ...account.models import User


class CustomerFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(
        label=_('ID'), field_name='id', lookup_expr='exact')
    full_name = django_filters.CharFilter(
        label=_('Full name'), method='filter_full_name')
    email = django_filters.CharFilter(
        label=_('Email'), field_name='email', lookup_expr='exact')

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name',
        ]

    def filter_full_name(self, queryset, name, value):
        for term in value.split():
            queryset = queryset.filter(
                Q(first_name__icontains=term) | Q(last_name__icontains=term))
        return queryset


class StaffFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(
        label=_('ID'), field_name='id', lookup_expr='exact')
    full_name = django_filters.CharFilter(
        label=_('Full name'), method='filter_full_name')
    email = django_filters.CharFilter(
        label=_('Email'), field_name='email', lookup_expr='exact')

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name',
        ]

    def filter_full_name(self, queryset, name, value):
        for term in value.split():
            queryset = queryset.filter(
                Q(first_name__icontains=term) | Q(last_name__icontains=term))
        return queryset
