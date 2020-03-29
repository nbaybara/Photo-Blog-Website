from django.contrib import admin

# Register your models here.
from post.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price','amount','status']
    list_filter = ['status', 'category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

