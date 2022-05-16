from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
from django.contrib.admin.views.decorators import (
    staff_member_required as _staff_member_required
)


def staff_member_required(f):
    return _staff_member_required(f, login_url='dashboard:login')


def get_paginator_items(items, paginate_by, page_number):
    if not page_number:
        page_number = 1
    paginator = Paginator(items, paginate_by)
    try:
        page_number = int(page_number)
    except ValueError:
        raise Http404('Page can not be converted to an int.')

    try:
        items = paginator.page(page_number)
    except InvalidPage as err:
        raise Http404('Invalid page (%(page_number)s): %(message)s' % {
            'page_number': page_number, 'message': str(err)})
    return items