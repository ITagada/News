# Generated by Django 5.0 on 2023-12-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('age', models.IntegerField()),
                ('born_at', models.DateField()),
                ('photo', models.ImageField(upload_to='media/%Y/%m/%d')),
            ],
        ),
    ]
