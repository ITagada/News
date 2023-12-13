from django.db import models


class Human(models.Model):
    human_choices = {'m': 'male',
                     'f': 'female'}

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=human_choices)
    age = models.IntegerField()
    born_at = models.DateField()
    photo = models.ImageField(upload_to='media/%Y/%m/%d', default='Null')
