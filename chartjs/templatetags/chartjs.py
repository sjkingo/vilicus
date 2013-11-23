from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def jsify_list(python_list):
    assert type(python_list) == list

    r = '['
    for i, entry in enumerate(python_list):
        if type(entry) == int:
            e = str(entry)
        else:
            e = '"' + entry + '"'
        if i+1 != len(python_list):
            e += ', '
        r += e
    r += ']'

    return mark_safe(r)

@register.inclusion_tag('chartjs/line_chart.html')
def line_chart(canvas_id, chart_config=None, width='400', height='400'):
    if chart_config is None:
        raise template.TemplateSyntaxError('chart_config argument must be provided and not None')

    return {
        'canvas_id': canvas_id,
        'canvas_width': width,
        'canvas_height': height,
        'labels': jsify_list(chart_config['xaxis']),
        'dataset': jsify_list(chart_config['dataset']),
    }
