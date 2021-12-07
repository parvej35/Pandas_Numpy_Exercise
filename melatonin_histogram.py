from random import randint

import bokeh
import numpy as np
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.models import CategoricalColorMapper, HoverTool, ColumnDataSource, Panel
from bokeh.models.widgets import CheckboxGroup, Slider, RangeSlider, Tabs
from bokeh.palettes import Category20_16
from bokeh.plotting import figure

df_parvej = df_thijs = df_jan = pd.DataFrame(
    columns=["Subject", "Start Time", "End Time", "Minutes Asleep", "Minutes Awake", "Number of Awakenings",
             "Time in Bed", "Minutes REM Sleep", "Minutes Light Sleep", "Minutes Deep Sleep"])

df_parvej = pd.read_csv("data/fitbit_export_202111_parvej.csv")
df_thijs = pd.read_csv("data/fitbit_export_202111_thijs.csv")
df_jan = pd.read_csv("data/fitbit_export_202111_jan.csv")
df_milad = pd.read_csv("data/fitbit_export_202111_milad.csv")
df_maryam = pd.read_csv("data/fitbit_export_202111_maryam.csv")

df_parvej = df_parvej.loc[::-1, :]
df_thijs = df_thijs.loc[::-1, :]
df_jan = df_jan.loc[::-1, :]
df_milad = df_milad.loc[::-1, :]
df_maryam = df_maryam.loc[::-1, :]

# print(df_jan)
""" Split Sleep start and end time"""

df_parvej[["End Date", "End Time"]] = df_parvej["End Time"].str.split(" ", n=1, expand=True)
# df_parvej["End Date"] = df_parvej["End Date"]
df_parvej["End Date"] = pd.to_datetime(df_parvej["End Date"])
df_parvej["End Time"] = df_parvej["End Time"]
# df_parvej.drop(columns=["End Time"], inplace=True)
df_parvej["subject_name"] = "Subject 1"

df_thijs[["End Date", "End Time"]] = df_thijs["End Time"].str.split(" ", n=1, expand=True)
# df_thijs["End Date"] = df_thijs["End Date"]
df_thijs["End Date"] = pd.to_datetime(df_thijs["End Date"])
df_thijs["End Time"] = df_thijs["End Time"]
# df_thijs.drop(columns=["End Time"], inplace=True)
df_thijs["subject_name"] = "Subject 2"

df_jan[["End Date", "End Time"]] = df_jan["End Time"].str.split(" ", n=1, expand=True)
# df_jan["End Date"] = df_jan["End Date"]
df_jan["End Date"] = pd.to_datetime(df_jan["End Date"])
df_jan["End Time"] = df_jan["End Time"]
df_jan["subject_name"] = "Subject 3"
# df_jan.drop(columns=["End Time"], inplace=True)

df_milad[["End Date", "End Time"]] = df_milad["End Time"].str.split(" ", n=1, expand=True)
# df_milad["End Date"] = df_jan["End Date"]
df_milad["End Date"] = pd.to_datetime(df_milad["End Date"])
df_milad["End Time"] = df_milad["End Time"]
df_milad["subject_name"] = "Subject 4"
# df_jan.drop(columns=["End Time"], inplace=True)

df_maryam[["End Date", "End Time"]] = df_maryam["End Time"].str.split(" ", n=1, expand=True)
# df_maryam["End Date"] = df_maryam["End Date"]
df_maryam["End Date"] = pd.to_datetime(df_maryam["End Date"])
df_maryam["End Time"] = df_maryam["End Time"]
df_maryam["subject_name"] = "Subject 5"
# df_maryam.drop(columns=["End Time"], inplace=True)

""" End: Split Sleep start and end time"""

date_array = df_thijs.loc[:, "End Date"].to_numpy()

# parvej_total_asleep_array = df_parvej.loc[:, "Minutes Asleep"].to_numpy()
# thijs_total_asleep_array = df_thijs.loc[:, "Minutes Asleep"].to_numpy()
# jan_total_asleep_array = df_jan.loc[:, "Minutes Asleep"].to_numpy()

# print(df_thijs.dtypes)
# print(df_parvej.head())
# print(df_jan.dtypes)
# print(df_jan.head())

# final_df1 = [df_parvej, df_thijs, df_jan, df_milad, df_maryam]
final_df = pd.concat([df_parvej, df_thijs, df_jan, df_milad, df_maryam])

# print(final_df)
# print(final_df.dtypes)

# Available carrier list
available_subjects = list(final_df['subject_name'].unique())
# print("\navailable_subjects:")
# print(available_subjects)

# Sort the list in-place (alphabetical order)
available_subjects.sort()


# print(available_subjects)


# Dataset based on selected carriers, selected start and end of delays,
# and selected width of bin
def make_dataset(carrier_list, range_start, range_end, bin_width):
    # print("\nA1:")
    # print(carrier_list)

    # print("\nA2:")
    # print(range_start)

    # print("\nA3:")
    # print(range_end)
    # print("\nA4:")
    # print(bin_width)

    by_carrier = pd.DataFrame(columns=['End Date', 'Minutes Asleep', 'Minutes Awake', 'Number of Awakenings ',
                                       'Minutes REM Sleep', 'Minutes Deep Sleep', 'Minutes Light Sleep'])

    # print("\nA5:")
    range_extent = range_end - range_start
    # print("\nA6:")
    # Iterate through all the carriers
    for i, carrier_name in enumerate(carrier_list):
        # print("\nA7: " + carrier_name)
        # Subset to the carrier
        subset = final_df[final_df['subject_name'] == carrier_name]

        # Create a histogram with 5 minute bins
        arr_hist, edges = np.histogram(subset['Minutes Asleep'],
                                       bins=int(range_extent / bin_width),
                                       range=[range_start, range_end])

        # print(arr_hist)
        # print(edges)
        # print("\nA8: " + carrier_name)

        # Divide the counts by the total to get a proportion
        arr_df = pd.DataFrame({'proportion': arr_hist / np.sum(arr_hist), 'left': edges[:-1], 'right': edges[1:]})
        # print("\nA9: " + carrier_name)

        # Format the proportion
        arr_df['sleeping_score'] = randint(65, 80)  # @Todo -??????????
        # arr_df['sleeping_score'] = ['%0.5f' % proportion for proportion in arr_df['proportion']]
        # print("\nA10: " + carrier_name)

        # Format the interval
        arr_df['minutes_asleep'] = subset['Minutes Asleep']
        # arr_df['minutes_asleep'] = ['%d to %d minutes' % (left, right) for left, right in zip(arr_df['left'], arr_df['right'])]
        # print("\nA11: " + carrier_name)

        # Assign the carrier for labels
        arr_df['name'] = carrier_name
        # print("\nA12: " + carrier_name)

        # Color each carrier differently
        arr_df['color'] = Category20_16[i]
        # print("\nA13: " + carrier_name)

        # Add to the overall dataframe
        by_carrier = by_carrier.append(arr_df)
        # print("\nA14: " + carrier_name)

    # Overall dataframe
    # by_carrier = by_carrier.sort_values(['subject_name', 'left'])

    # print("\nA15: ")
    # by_carrier = by_carrier.sort_values(['subject_name'])

    # print("\nA16: ")
    return ColumnDataSource(by_carrier)


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


# Function to make the plot
def make_plot(src):
    # print(src)
    # Blank plot with correct labels
    p = figure(plot_width=1000, plot_height=500,
               title='Sleeping data by Subject',
               x_axis_label='Date', y_axis_label='Sleeping Duration (min)')

    # Quad glyphs to create a histogram
    # p.quad(source=src, bottom=0, top='proportion', left='left', right='right',
    #        color='color', fill_alpha=0.7, hover_fill_color='color', legend_label='name',
    #        hover_fill_alpha=1.0, line_color='black')

    p.quad(source=src, bottom=0, top='proportion', left='left', right='right',
           color='color', fill_alpha=70, hover_fill_color='color',
           hover_fill_alpha=100, line_color='black')

    # Hover tool with vline mode
    hover = HoverTool(tooltips=[('Name', '@name'),
                                ('Minutes Asleep', '@minutes_asleep'),
                                ('Sleeping Score', '@sleeping_score')],
                      mode='vline')

    p.add_tools(hover)

    p.legend.click_policy = 'hide'

    # Styling
    p = style(p)

    return p


# Update the plot based on selections
def update(attr, old, new):
    # print(old)
    # print(new)

    carriers_to_plot = [carrier_selection.labels[i] for i in carrier_selection.active]

    # new_src = make_dataset(carriers_to_plot, range_start=range_select.value[0], range_end=range_select.value[1], bin_width=5)
    new_src = make_dataset(carriers_to_plot, range_start=range_select.value[0], range_end=range_select.value[1],
                           bin_width=binwidth_select.value)

    src.data.update(new_src.data)


# print("\nP3:")
carrier_selection = CheckboxGroup(labels=available_subjects, active=[0, 1])
carrier_selection.on_change('active', update)

# print("\nP4:")

# Slider to select width of bin
binwidth_select = Slider(start=1, end=10, step=1, value=5, title='Width')
binwidth_select.on_change('value', update)

# range_select = RangeSlider(start=-60, end=180, value=(-60, 120), step=5, title='Delay Range (min)')
range_select = RangeSlider(start=1, end=1000, value=(0, 1000), step=10, title='Sleeping Time (min)')
range_select.on_change('value', update)

initial_carriers = [carrier_selection.labels[i] for i in carrier_selection.active]

# print("\nP1:")
# print(initial_carriers)

# src = make_dataset(initial_carriers, range_start=range_select.value[0], range_end=range_select.value[1], bin_width=5)
src = make_dataset(initial_carriers, range_start=range_select.value[0], range_end=range_select.value[1],
                   bin_width=binwidth_select.value)

print(initial_carriers)
print(src)
# print("\nP2:")
p = make_plot(src)

# Put controls in a single element
# controls = bokeh.models.Column(carrier_selection, 5, range_select)
controls = bokeh.models.Column(carrier_selection, binwidth_select, range_select)

# Create a row layout
layout = row(controls, p)

# Make a tab with the layout
tab = Panel(child=layout, title='Melatonin Group')
tabs = Tabs(tabs=[tab])

# Add it to the current document (displays plot)
curdoc().add_root(tabs)
