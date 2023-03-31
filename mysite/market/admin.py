from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'price', 'stock', 'available', 'description', 'category', 'image', 'created',
                    'updated')
    list_filter = ('title','available', 'created', 'updated')
    list_editable = ('title', 'slug', 'price', 'stock', 'available', 'description', 'category', 'image')
    list_display_links = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
