from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

#@register.filter(name = 'custom name')
# @register.filter
# def to_lowerCase(value):
#     return value.lower()

@register.filter
def to_lowerCase(value, arg):
    return f'{arg} : {value[0].upper()}{value[1:]}'

