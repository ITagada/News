from django.db import models
from django.urls import reverse_lazy


class Human(models.Model):
    human_choices = {'m': 'male',
                     'f': 'female'}

    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    sex = models.CharField(max_length=1, choices=human_choices, verbose_name='Пол')
    age = models.IntegerField(verbose_name='Возраст')
    born_at = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', null=True, default='Null', verbose_name='Фото')
    profession = models.ForeignKey('profession', on_delete=models.PROTECT, null=True, verbose_name='Профессия')

    def get_absolut_url(self):
        return reverse_lazy('view_human', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
        ordering = ['-born_at']


class Profession(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Профессия')

    def get_absolut_url(self):
        return reverse_lazy('profession', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['title']
