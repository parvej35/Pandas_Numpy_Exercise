import pandas as pd
import numpy as np

data_file_dict = {
    "Parvej": "data/fitbit_export_202111_parvej_1.csv",
    # "Thijs": "data/fitbit_export_202111_thijs.csv",
    # "Jan": "data/fitbit_export_202111_jan.csv",
}

"""
lines = []
for key, value in data_file_dict.items():
    print(key + " -> " + value)

    with open(value, "r") as txt_file:
        line_counter = 1
        for line in txt_file:

            if line_counter > 1:
                lines.append(line)

            line_counter += 1

print(lines)
"""

df = pd.DataFrame(
    columns=["Subject", "Start Time", "End Time", "Minutes Asleep", "Minutes Awake", "Number of Awakenings",
             "Time in Bed", "Minutes REM Sleep", "Minutes Light Sleep", "Minutes Deep Sleep"])

for key, value in data_file_dict.items():
    dataFrame1 = pd.read_csv(value)
    dataFrame1["Subject"] = key

    df = df.append(dataFrame1)

df = df.loc[::-1, :]
print(df)
""" Split Sleep start and end time"""

df[["Start Date", "Start Time"]] = df["Start Time"].str.split(" ", n=1, expand=True)
df["Start Date"] = df["Start Date"]
df["Start Time"] = df["Start Time"]
# df.drop(columns=["Start Time"], inplace=True)

df[["End Date", "End Time"]] = df["End Time"].str.split(" ", n=1, expand=True)
df["End Date"] = df["End Date"]
df["End Time"] = df["End Time"]
# df.drop(columns=["End Time"], inplace=True)

""" End: Split Sleep start and end time"""

# print(df)

# df['End Date'] = pd.to(df['End Date'])
# start_date = '01-11-2021'
# end_date = '15-11-2021'
# df = (df['End Date'] > start_date) & (df['End Date'] <= end_date)
# print(df)

# print(df.loc[:, ["End Date", "Minutes REM Sleep", "Minutes Light Sleep", "Minutes Deep Sleep", "Minutes Asleep"]])
date_array = df.loc[:, "End Date"].to_numpy()
rem_sleep_array = df.loc[:, "Minutes REM Sleep"].to_numpy()
light_sleep_array = df.loc[:, "Minutes Light Sleep"].to_numpy()
deep_sleep_array = df.loc[:, "Minutes Deep Sleep"].to_numpy()
total_asleep_array = df.loc[:, "Minutes Asleep"].to_numpy()

print(date_array)

# print(df.head(50))

print(df.loc[5])
# print(df.iloc[5])


import matplotlib.pyplot as plot

# A python dictionary
data = {"REM Sleep": rem_sleep_array, "Light Sleep": light_sleep_array, "Deep Sleep": deep_sleep_array}
index = date_array

# Dictionary loaded into a DataFrame
df = pd.DataFrame(data=data, index=index)

# Draw a vertical bar chart
df.plot.bar(stacked=True, rot=15, title="Subject-1 Sleeping Data (01-Nov-2021 ~ 10-Nov-2021)")

# plot.xlabel('x')
# plot.ylabel('y')
# plot.grid(color='lightgray', linestyle='dashed')
plot.grid(True, color="gray", linewidth="0.1", linestyle='dashed')

for index, data in enumerate(total_asleep_array):
    plot.text(x=index, y=data + 1, s=f"{data}")

# for i, v in enumerate(total_asleep_array):
# plot.text(v, i, str(v), color='blue', fontweight='bold')
# plot.text(v, i, " " + str(v), color='blue', va='center', fontweight='bold')

plot.show(block=True)
# plot.show()
