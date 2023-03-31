from .cart_model import Cart


def cart(request):
    return {'cart': Cart(request)}
