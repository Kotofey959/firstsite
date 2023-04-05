from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import DataMixin
from .cart_model import Cart


class MarketHome(DataMixin, ListView):
    paginate_by = 10
    model = Product
    template_name = 'mymarket/home.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(available=True)


class ProductView(DataMixin, DetailView):
    model = Product
    template_name = 'mymarket/show_product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_form = CartAddProductForm()
        c_def = self.get_user_context(title=context['product'], cart_form=cart_form)
        return dict(list(context.items()) + list(c_def.items()))


class CategoryView(DataMixin, ListView):
    model = Product
    template_name = 'mymarket/show_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mymarket/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


def login(request):
    return render(request, 'mymarket/contact.html')


@require_POST
def cart_add(request, product_id, count=1):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart.add(product=product,
                 quantity=count,
                 update_quantity=data['update'])
    return redirect('cart')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
        return render(request, 'order/create.html',
                      {'cart': cart, 'form': form})
