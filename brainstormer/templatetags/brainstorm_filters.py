from django import template

register = template.Library()


@register.filter(name='int_to_string')
def int_to_string(integer):
    return str(integer)