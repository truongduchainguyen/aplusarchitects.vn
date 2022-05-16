import django.http.request
from django.contrib.sites.shortcuts import get_current_site
from .models import SocialNetwork


def site(request):
    site = get_current_site(request)
    social_network_list = SocialNetwork.objects.all().order_by('-id')
    return {'site': site, 'social_network_list': social_network_list}
