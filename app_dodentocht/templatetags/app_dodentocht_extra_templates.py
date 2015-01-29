# This template tag makes sure you can access lists per index in html template
from django import template
register = template.Library()


# This filter makes sure you can access lists in template tags
@register.filter
def get_at_index(list, index):
    return list[index-1] # "index-1" because forloop.counter in django template is 1-indexed

@register.filter(name='jsdate')
def jsdate(d):
    """formats a python date into a js Date() constructor.
    """
    try:
        return "new Date({0},{1},{2})".format(d.year, d.month - 1, d.day)
    except AttributeError:
        return 'undefined'