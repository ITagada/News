from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from .forms import HumanForm, UserRegisterForm, UserLoginForm
from .models import Human, Profession
from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Упс! Что-то пошло не так!')
    else:
        form = UserRegisterForm()
    return render(request, 'NewsProject/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'NewsProject/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('Login')


class HomeHuman(ListView, MyMixin):
    model = Human
    context_object_name = 'human'
    template_name = 'NewsProject/Humans.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['mixin_group'] = self.get_prop()
        return context

    def get_queryset(self):
        return Human.objects.filter(age__range=(26, 40)).select_related('profession')


class HumanProfession(ListView):
    model = Human
    template_name = 'NewsProject/Profession.html'
    context_object_name = 'human'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profession = get_object_or_404(Profession, pk=self.kwargs['pk'])
        context['professions'] = profession
        context['title'] = profession.title
        return context

    def get_queryset(self):
        profession = get_object_or_404(Profession, pk=self.kwargs['pk'])
        return Human.objects.filter(profession=profession).select_related('profession')


class ViewHuman(DetailView):
    model = Human
    template_name = 'NewsProject/view_human.html'
    context_object_name = 'human_item'


class AddHuman(CreateView):
    model = Human
    form_class = HumanForm
    template_name = 'NewsProject/add_human.html'
    login_url = '/admin/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('view_human', pk=self.object.pk)

# def index(request):
#     human = Human.objects.all()
#     professions = Profession.objects.all()
#     context = {
#         'human': human,
#         'title': 'Люди'
#     }
#     return render(request, 'NewsProject/Humans.html', context=context)


# def get_profession(request, profession_id):
#     human = Human.objects.filter(profession_id=profession_id)
#     professions = Profession.objects.all()
#     profession = Profession.objects.get(pk=profession_id)
#     context = {
#         'human': human,
#         'profession': profession
#     }
#     return render(request, 'NewsProject/Profession.html', context=context)


# def view_human(request, human_id):
#     # human_item = Human.object.get(pk=human_id)
#     human_item = get_object_or_404(Human, pk=human_id)
#     context = {
#         'human_item': human_item
#     }
#     return render(request, 'NewsProject/view_human.html', context=context)


# def add_human(request):
#     if request.method == 'POST':
#         form = HumanForm(request.POST)
#         if form.is_valid():
#             # human = Human.objects.create(**form.cleaned_data)
#             human = form.save()
#             return redirect(human)
#     else:
#         form = HumanForm()
#     return render(request, 'NewsProject/add_human.html', {'form': form})
