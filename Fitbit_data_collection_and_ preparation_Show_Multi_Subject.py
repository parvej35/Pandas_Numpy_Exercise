import pandas as pd
import numpy as np

df_parvej = df_thijs = df_jan = pd.DataFrame(
    columns=["Subject", "Start Time", "End Time", "Minutes Asleep", "Minutes Awake", "Number of Awakenings",
             "Time in Bed", "Minutes REM Sleep", "Minutes Light Sleep", "Minutes Deep Sleep"])

df_parvej = pd.read_csv("data/fitbit_export_202111_parvej_1.csv")
df_thijs = pd.read_csv("data/fitbit_export_202111_thijs_1.csv")
df_jan = pd.read_csv("data/fitbit_export_202111_jan_1.csv")

df_parvej = df_parvej.loc[::-1, :]
df_thijs = df_thijs.loc[::-1, :]
df_jan = df_jan.loc[::-1, :]

# print(df_jan)
""" Split Sleep start and end time"""

df_parvej[["End Date", "End Time"]] = df_parvej["End Time"].str.split(" ", n=1, expand=True)
df_parvej["End Date"] = df_parvej["End Date"]
df_parvej["End Time"] = df_parvej["End Time"]
# df_parvej.drop(columns=["End Time"], inplace=True)

df_thijs[["End Date", "End Time"]] = df_thijs["End Time"].str.split(" ", n=1, expand=True)
df_thijs["End Date"] = df_thijs["End Date"]
df_thijs["End Time"] = df_thijs["End Time"]
# df_thijs.drop(columns=["End Time"], inplace=True)

df_jan[["End Date", "End Time"]] = df_jan["End Time"].str.split(" ", n=1, expand=True)
df_jan["End Date"] = df_jan["End Date"]
df_jan["End Time"] = df_jan["End Time"]
# df_jan.drop(columns=["End Time"], inplace=True)

""" End: Split Sleep start and end time"""

date_array = df_thijs.loc[:, "End Date"].to_numpy()

parvej_total_asleep_array = df_parvej.loc[:, "Minutes Asleep"].to_numpy()
thijs_total_asleep_array = df_thijs.loc[:, "Minutes Asleep"].to_numpy()
jan_total_asleep_array = df_jan.loc[:, "Minutes Asleep"].to_numpy()

print(parvej_total_asleep_array)
print(thijs_total_asleep_array)
print(jan_total_asleep_array)

# print(df.head(50))

import matplotlib.pyplot as plot

# A python dictionary

data = {"Jan": jan_total_asleep_array, "Thijs": thijs_total_asleep_array, "Parvej": parvej_total_asleep_array}
index = date_array

# Dictionary loaded into a DataFrame
dataFrame = pd.DataFrame(data=data, index=index)

# Draw a vertical bar chart
dataFrame.plot.bar(rot=45, title="Total Sleep Duration (Jan vs Thijs vs Parvej)");
plot.grid(True, color="gray", linewidth="0.4", linestyle='dashed')
plot.show(block=True);