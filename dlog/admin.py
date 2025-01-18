from django.contrib import admin
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
    list_display = ['title', 'slug', 'category', 'is_active', 'is_recent', 'is_banner', 'is_featured', 'created_at']
    list_filter = ['category', 'is_active', 'is_banner', 'is_recent', 'is_featured']
    list_editable = ['category', 'is_active', 'is_banner', 'is_recent', 'is_featured']
    list_display_links = ['title', 'slug']
    search_fields = ['title', 'slug', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

# Register your models here.
