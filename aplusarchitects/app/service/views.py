from django.shortcuts import render
from .models import Service


def index(request):
    services = Service.objects.all().order_by('sort_order')
    ctx = {'services': services}
    return render(request, 'service/index.html', ctx)
