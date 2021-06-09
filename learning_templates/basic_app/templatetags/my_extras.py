from django import template
register = template.Library()

# directly using decorator instead of below line.that means decorator(cut)=cut.i.e,fun'cut =fun'filter(fun'cut)
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
# 1st cut is the name i gave to my filter and 2nd cut is the function cut that i created above
