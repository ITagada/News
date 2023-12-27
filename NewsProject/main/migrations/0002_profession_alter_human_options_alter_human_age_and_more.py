# Generated by Django 5.0 on 2023-12-19 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Профессия')),
            ],
        ),
        migrations.AlterModelOptions(
            name='human',
            options={'ordering': ['-born_at'], 'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterField(
            model_name='human',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='human',
            name='born_at',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='human',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='human',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='human',
            name='photo',
            field=models.ImageField(default='Null', null=True, upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='human',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='human',
            name='profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.profession',
                                    verbose_name='Профессия'),
        ),
    ]