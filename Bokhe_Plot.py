import random

import bokeh
from bokeh.io import output_file, show
from bokeh.layouts import column, row
from bokeh.models import Range1d
from bokeh.models.widgets import Panel, Tabs, CheckboxGroup, Div
from bokeh.plotting import figure

# output_file("issue.html")


# Styling for a plot
def style(p):
    # Title
    p.title.align = 'center'
    p.title.text_font_size = '20pt'
    p.title.text_font = 'serif'

    # Axis titles
    p.xaxis.axis_label_text_font_size = '14pt'
    p.xaxis.axis_label_text_font_style = 'bold'
    p.yaxis.axis_label_text_font_size = '14pt'
    p.yaxis.axis_label_text_font_style = 'bold'

    # Tick labels
    p.xaxis.major_label_text_font_size = '12pt'
    p.yaxis.major_label_text_font_size = '12pt'

    return p


# Update the plot based on selections
def update(attr, old, new):
    print(old)
    print(new)


def get_plot():
    p = figure(width=1000, height=500)
    xs = [x for x in range(20)]
    ys = [x * y for x, y in zip(xs, [random.randrange(-4, 4) for _ in range(len(xs))])]
    max_y = max(ys)
    min_y = min(ys)
    p.y_range = Range1d(0 + min_y * 1.1, max_y * 1.1)
    p.line(xs, ys)
    description = Div(text="""<h3>Choose Subject:</h3>""")
    checkbox_group = CheckboxGroup(
        labels=[f"Subject {x}" for x in range(1, 6)],
        css_classes=["scrollable"]
    )
    checkbox_group.on_change('active', update)

    return column(row(bokeh.models.Column(description, checkbox_group), p))


tabs = []
# for ii, tab_name in enumerate([f"some_random_tab_name_{i}" for i in range(5)]):
#     plot = get_plot()
#     tabs.append(Panel(child=plot, title=tab_name))


plot = get_plot()
tabs.append(Panel(child=plot, title="Melatonin"))

tabs = Tabs(tabs=tabs)
# show(row(tabs))
