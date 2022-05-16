from django.shortcuts import render
from .data import TEAM_MEMBERS
from ..portfolio.models import Project
from ..service.models import Service


def index(request):
    list_featured = Project.objects.filter(is_featured=True)[:3]
    ctx = {'list_featured': list_featured}
    return render(request, 'index.html', ctx)


def about(request):
    services = Service.objects.all().order_by('sort_order')
    ctx = {'teams': TEAM_MEMBERS, 'services': services}
    return render(request, 'about.html', ctx)
