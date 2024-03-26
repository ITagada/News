from django.db.models import Count
from django import template
from django.core.cache import cache

from ..models import Profession


register = template.Library()


@register.simple_tag(name='get_list_professions')
def get_professions():
    return Profession.objects.all()


@register.inclusion_tag('NewsProject/List_professions.html')
def show_professions(arg1='Список', arg2='профессий'):
    professions = cache.get('professions')
    if not professions:
        professions = Profession.objects.annotate(cnt=Count('human')).filter(cnt__gt=0)
        cache.set('professions', professions, 60)
    return {'professions': professions, 'arg1': arg1, 'arg2': arg2}
