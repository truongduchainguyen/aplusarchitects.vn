from django.contrib.sites.models import Site
from django.conf import settings
from urllib.parse import urljoin
from django.utils.encoding import iri_to_uri
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404


def build_absolute_uri(location):
    host = Site.objects.get_current().domain
    protocol = 'https' if settings.ENABLE_SSL else 'http'
    current_uri = '%s://%s' % (protocol, host)
    location = urljoin(current_uri, location)
    return iri_to_uri(location)


def get_email_base_context():
	site = Site.objects.get_current()
	return {
        'domain': site.domain,
        'site_name': site.name
    }


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
