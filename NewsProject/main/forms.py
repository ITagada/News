from django import forms
from .models import Profession, Human
import re
from django.core.exceptions import ValidationError


class HumanForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValueError('Имя не должно начинаться с цифр')
        return name

    class Meta:
        human_choices = {'m': 'male',
                         'f': 'female'}
        model = Human
        # fields = '__all__'
        fields = ['name', 'last_name', 'sex', 'age', 'born_at', 'profession']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'sex': forms.Select(attrs={
                'class': 'form-control'
            }),
            'age': forms.NumberInput(),
            'born_at': forms.SelectDateWidget(empty_label=("Выберите год", "Выберите месяц", "Выберите день"),
                                              years=range(1900, 2023),
                                              attrs={
                                                  'class': 'form-control'
                                              }),
            'profession': forms.Select(attrs={
                'class': 'form-control'
            })
        }
