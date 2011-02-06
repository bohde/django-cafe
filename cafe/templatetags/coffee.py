from django import template

from cafe.compiler import Compiler

register = template.Library()

@register.tag
def coffee(parser, token):
    try:
        tokens = token.split_contents()
        tag_name, files = tokens[0], tokens[1:]
    except IndexError:
        raise template.TemplateSyntaxError, "%s tag requires at least one filename." % tag_name
    return CoffeeNode(files)


class CoffeeNode(template.Node):
    def __init__(self, files):
        self.compiler = Compiler(files)
    
    def render(self, context):
        return self.compiler.compile()
