import bokeh
import numpy as np
import pandas as pd
from bokeh.io import output_file, show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel
from bokeh.models.widgets import Panel, Tabs, CheckboxGroup, Div
from bokeh.plotting import figure

import bokeh.io
bokeh.io.output_notebook()

output_file("slider.html")


def checkbox_click_handler(selected_checkboxes):
    print(selected_checkboxes)


def get_plot():
    description = Div(text="""<h3>Choose Subject:</h3>""")
    checkbox_group = CheckboxGroup(
        labels=[f"Subject {x}" for x in range(5)],
        css_classes=["scrollable"],
    )
    #checkbox_group.on_click(checkbox_click_handler)
    return bokeh.models.Column(description, checkbox_group, sizing_mode='stretch_both')
    # return bokeh.models.Column(description, checkbox_group)


plot = get_plot()

p1 = figure(plot_width=500, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

p2 = figure(plot_width=500, plot_height=300)
p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=1, color="navy", alpha=0.5)

layout = row(plot, p1, p2)

show(layout)
