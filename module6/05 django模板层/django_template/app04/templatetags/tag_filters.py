from django import template


register = template.Library()


@register.filter
def multi_filter(x,y):
    return x*y


@register.simple_tag
def multi_tag(x,y):
    return x*y

