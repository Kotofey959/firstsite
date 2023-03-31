from django.db.models import Count

from .models import *

menu = [
        {'title': "Корзина", 'url_name': 'cart'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('product'))
        user_menu = menu.copy()

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


