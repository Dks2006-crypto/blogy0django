# Generated by Django 5.1.5 on 2025-01-18 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL - ссылка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название тега')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL - ссылка')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название поста')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL - ссылка')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Отображать на сайте')),
                ('is_banner', models.BooleanField(default=False, help_text='Данная запись будет отображаться в баннере на главной странице', verbose_name='Отображать в баннере')),
                ('is_recent', models.BooleanField(default=False, help_text='Данная запись будет отображаться в разделе новинки', verbose_name='Новая запись')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Рекомендуемая запись')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlog.category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(to='dlog.tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя автора')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=False, verbose_name='Отображать на сайте')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dlog.post', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-pk'],
            },
        ),
    ]
