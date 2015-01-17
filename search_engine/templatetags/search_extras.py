from django import template

register = template.Library()

@register.filter
def keyvalue(dict, key):
    if key in dict:
        return dict[key]
    else:
        return False