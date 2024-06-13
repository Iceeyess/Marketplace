from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def get_path_for_media(data):
    if data:
        return f"/media/{data}"
    return "{% static 'apology.webp' %}"


# Создание фильтра
@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "<strong>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)