from django import template

register = template.Library()

def Joyan_Cut (value, arg):
    """
    This custom temlate tag function cuts out all values in arg from value out.
    """
    return value.replace(arg, '')

register.filter('Joyans_Cut_func', Joyan_Cut)
