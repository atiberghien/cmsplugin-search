from django import template
from haystack.forms import ModelSearchForm
register = template.Library()

@register.inclusion_tag('search/search_form.html')
def show_search_widget():
    return {'form' : ModelSearchForm(load_all=True)}
    