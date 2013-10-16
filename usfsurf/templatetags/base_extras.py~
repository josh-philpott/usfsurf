# Code from Alon Swartz at http://www.turnkeylinux.org/blog/django-navbar
from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive (request, pattern):
    import re
    print pattern + " | " + request.path
    if re.search(pattern, request.path) and pattern != '':
	print "got it"
        return 'active'
    return ''
