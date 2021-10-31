from django import template

register = template.Library()

@register.filter(name='add_class')
def addclass(value, arg):
    print("Hello",type(value), type(arg))
    return value.as_widget(attrs={'class':arg})
