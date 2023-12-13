from django.shortcuts import render

from .models import Human


def index(request):
    human = Human.objects.all()
    return render(request, 'NewsProject/Humans.html', {'human': human, 'title': 'Люди'})
