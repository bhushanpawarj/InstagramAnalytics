from django import template

register=template.Library()
@register.filter(is_safe=True)

def modulo(n ):
    return  n%4
