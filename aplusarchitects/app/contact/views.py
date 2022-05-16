from django.shortcuts import render


def index(request):
    ctx = {}
    return render(request, 'contact/index.html', ctx)
