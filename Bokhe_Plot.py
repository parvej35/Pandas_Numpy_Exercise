import random

import bokeh
from bokeh.io import output_file, show
from bokeh.layouts import column, row
from bokeh.models import Range1d
from bokeh.models.widgets import Panel, Tabs, CheckboxGroup, Div
from bokeh.plotting import figure

output_file("issue.html")


def get_plot():
    p = figure(width=1000, height=500)
    xs = [x for x in range(20)]
    ys = [x * y for x, y in zip(xs, [random.randrange(-4, 4) for _ in range(len(xs))])]
    max_y = max(ys)
    min_y = min(ys)
    p.y_range = Range1d(0 + min_y * 1.1, max_y * 1.1)
    p.line(xs, ys)
    description = Div(text="""<h3>Choose something:</h3>""")
    checkbox_group = CheckboxGroup(
        labels=[f"pick option {x}" for x in range(5)],
        css_classes=["scrollable"]
    )

    return column(row(bokeh.models.Column(description, checkbox_group), p))


tabs = []
for ii, tab_name in enumerate([f"some_random_tab_name_{i}" for i in range(5)]):
    plot = get_plot()
    tabs.append(Panel(child=plot, title=tab_name))

tabs = Tabs(tabs=tabs)
show(row(tabs))
