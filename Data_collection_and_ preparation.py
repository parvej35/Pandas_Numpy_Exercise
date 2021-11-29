import pandas as pd
import numpy as np

# dataset = pd.read_csv("data/heart_failure_clinical_records_dataset.csv")
dataset = pd.read_csv("data/fitbit_export_202111_parvej.csv")

# dataset = dataset.drop(dataset.index[0])
# Show all column names
print(dataset.columns)

# Show top 5 rows
print(dataset.head())

# Show bottom 5 rows
# print(dataset.tail(5))

# Show only selected columns of the dataset
# temp_dataset = dataset[['age', 'diabetes', 'high_blood_pressure', 'platelets', 'time']]
# print(temp_dataset.head(5))

# Show total number of data rows X columns
print(dataset.shape)

# print(dataset.tail(10))
# print(dataset.describe())

# Drop the garbage data (index 299)
# dataset = dataset.drop(dataset.index[299])
# dataset.drop(dataset.index[299], inplace=True)
# print(dataset.tail())

# Convert ROW-> COLUMN & COLUMN-> ROW
print(dataset)
# dataset = dataset.transpose()
# print(dataset)

# Take a sample of randomly chosen 5 columns, because 300 takes too much memory
# temp_dataset = dataset.sample(5, axis="columns")
# print(temp_dataset)

# dataset.info()


