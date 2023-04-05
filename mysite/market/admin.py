from django.contrib import admin

from .models import Category, Product, OrderItem, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'price', 'stock', 'available', 'description', 'category', 'image', 'created',
                    'updated')
    list_filter = ('title','available', 'created', 'updated')
    list_editable = ('title', 'slug', 'price', 'stock', 'available', 'description', 'category', 'image')
    list_display_links = ('id',)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
