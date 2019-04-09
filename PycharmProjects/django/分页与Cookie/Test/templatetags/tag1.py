from django.utils.safestring import mark_safe
from django import template
register = template.Library() # 名称不能改


@register.simple_tag
def tag1(a,b):
    return a+b


@register.filter
def addstr(a,b):
    return a+b
