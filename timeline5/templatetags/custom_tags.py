# timeline/templatetags/custom_tags.py

from django import template

register = template.Library()

@register.filter
def range(value):
    return range(1, value + 1)
