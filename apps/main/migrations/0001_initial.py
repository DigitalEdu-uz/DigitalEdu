# Generated by Django 3.1.5 on 2021-02-09 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='contents/image/%Y_%m/', verbose_name='Фото')),
                ('name', models.CharField(max_length=50, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='contents/image/%Y_%m/', verbose_name='Фото')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('intro', models.TextField(verbose_name='Введение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('content', models.FileField(upload_to='contents/%Y_%m/', verbose_name='Контент')),
                ('url', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('draft', models.BooleanField(verbose_name='Черновик')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Имя ползователя и статус')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
