from django import template

register = template.Library()

@register.filter
def get_index(list_obj, index):
    try:
        return list_obj[index]
    except:
        return None
