from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории', blank=False)
    slug = models.SlugField(max_length=255, verbose_name='URL-ссылка', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега', blank=False)
    slug = models.SlugField(max_length=255, verbose_name='URL-ссылка', unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
# Create your models here.

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, verbose_name='Категория поста')
    tags = models.ManyToManyField(Tag, blank=False, verbose_name="Теги")
    title = models.CharField(max_length=255, verbose_name='Название поста', blank=False)
    slug = models.SlugField(max_length=255, verbose_name='URL-ссылка', unique=True)
    description = models.TextField(verbose_name='Краткое описание', blank=False)
    content = models.TextField(verbose_name='Контент', blank=False)
    image = models.ImageField(upload_to='posts/', verbose_name='Изображение', deafault='no-image.jpg', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Отображать на сайте')
    is_banner = models.BooleanField(default=True, verbose_name='Отображать в банере', help_text='Давнная запись будет отображаться на банере в главной странице')
    is_recent = models.BooleanField(default=False, verbose_name='Новая запись', help_text='Данная запись будет отображаться в разделе новинки')
    is_featured = models.BooleanField(default=False, verbose_name='Рекомендуемая запись')
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    name = models.CharField(max_length=255, verbose_name='Имя автора', blank=False)
    email = models.EmailField(max_length=255, verbose_name='Email', blank=False)
    content = models.TextField(verbose_name='Комментарий', blank=False)
    is_active = models.BooleanField(default=False, verbose_name='Отображать на сайте')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        overing = ['-pk']

    def __str__(self):
        return f'Комментарий от {self.name} к статье -{self.post}'