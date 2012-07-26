from django import template
from django.conf import settings
from django.utils.importlib import import_module
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType

register = template.Library()

class CustomResultNode(template.Node):
    def __init__(self, result_var):
        self.result_var = template.Variable(result_var)
    def render(self, context):
        result = self.result_var.resolve(context)
        current_model = type(result.object)

        for modelclass_path, template_name in dict(settings.CUSTOM_HAYSTACK_RESULT_TEMPLATES).iteritems():
            mod, modelname = modelclass_path.rsplit('.', 1)
            mod = import_module(mod)
            model = getattr(mod, modelname)
            
            if issubclass(current_model, model):
                return render_to_string(template_name=template_name, 
                                        dictionary={'result' : result},
                                        context_instance=context) 
        
        return ""
    
@register.tag(name="custom_result")
def custom_result(parser, token):
    if not hasattr(settings, "CUSTOM_HAYSTACK_RESULT_TEMPLATES"):
        raise AttributeError
    try:
        tag_name, param = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return CustomResultNode(param)