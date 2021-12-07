from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.models.widgets import Panel, Tabs, CheckboxGroup, Div

output_file("slider.html")

p1 = figure(plot_width=900, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
tab1 = Panel(child=p1, title="circle")

p2 = figure(plot_width=900, plot_height=300)
p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="navy", alpha=0.5)
tab2 = Panel(child=p2, title="line")

tabs = Tabs(tabs=[tab1, tab2])

layout = row(p1, p2)

show(layout)
