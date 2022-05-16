from django import template

register = template.Library()


@register.simple_tag()
def get_flag(lang_code):
    FLAG_CHOICES = (
        ('vi', 'flag-icon-vn'),
        ('en', 'flag-icon-us'),
    )
    return dict(FLAG_CHOICES).get(lang_code)
