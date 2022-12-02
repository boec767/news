from django.contrib import admin

from .models import Category, NewsBlog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(NewsBlog)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'img', 'category', 'user', 'content']
    prepopulated_fields = {'slug': ('title',)}
