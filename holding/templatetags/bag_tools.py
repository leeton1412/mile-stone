from django import template


register = template.Library()

@register.filter(name='calc_total')
def calc_total(price, quantity):
    return price * quantity