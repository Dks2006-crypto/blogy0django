from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['-pk']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['-pk']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image_tag', 'category', 'is_active', 'is_recent', 'is_banner', 'is_featured', 'created_at']
    list_filter = ['category', 'is_active', 'is_banner', 'is_recent', 'is_featured']
    list_editable = ['category', 'is_active', 'is_banner', 'is_recent', 'is_featured']
    list_display_links = ['title', 'slug']
    search_fields = ['title', 'slug', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60px" height="60px" style="border-radius:50%; object-fit:cover;" />'.format(obj.image.url))
        else:
            return None
    image_tag.short_description = 'Изображение'

# Register your models here.
