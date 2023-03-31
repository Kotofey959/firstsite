from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name='Изображение', blank=True, null=True)
    available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Количество')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={
            'category_slug': self.category.slug,
            'product_slug': self.slug,
            'product_id': self.id
        })


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
