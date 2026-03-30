from django import template
from apps.front.models import Home


register = template.Library()

@register.simple_tag
def get_info():
    obj = Home.objects.first()
    return obj