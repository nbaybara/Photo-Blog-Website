from django.contrib import admin

# Register your models here.
from post.models import Category, Post, Images


class PostImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [PostImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Images, ImagesAdmin)
