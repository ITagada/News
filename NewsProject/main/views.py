from django.shortcuts import render

from .models import Human, Profession


def index(request):
    human = Human.objects.all()
    professions = Profession.objects.all()
    context = {
        'human': human,
        'title': 'Люди'
    }
    return render(request, 'NewsProject/Humans.html', context=context)


def get_profession(request, profession_id):
    human = Human.objects.filter(profession_id=profession_id)
    professions = Profession.objects.all()
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'human': human,
        'profession': profession
    }
    return render(request, 'NewsProject/Profession.html', context=context)
