from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(productid,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==productid:
            pass
    pass


@register.filter(name='cart_quantity')
def cart_quantity(productid,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==productid:  
            return True;
    return cart.get(id)
    
