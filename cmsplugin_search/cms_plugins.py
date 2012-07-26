from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from .models import SearchPlugin
from haystack.forms import ModelSearchForm

class CMSSearchPlugin(CMSPluginBase):
    model = SearchPlugin
    name = _("Search") # Name of the plugin
    render_template = "search/search_form.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'form':ModelSearchForm(load_all=True)})
        return context

plugin_pool.register_plugin(CMSSearchPlugin) # register the plugin