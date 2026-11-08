"""
RECORD CHECK  -  my version
===========================

Name  : Anashe Neola Kabaya
Lane  :  AI 
Date  : 04/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

# creating dataframe with dataset
df = pd.DataFrame({"dataset": ["survey_2021", "survey_2022", "survey_2023", "survey_2024", "survey_2025"],
                   "rows_loaded": [1185, 1050, 1250, 1120, 1223],
                   "rows_expected": [1200, 1200, 1200, 1200, 1200], })

df.to_csv("my_file.csv", index=False) # saving the data as a CSV file

df = pd.read_csv("my_file.csv")   # reading data from the CSV file


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# calculating the percentages of each record (row) and storing them in the new column 'percent'
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

# Creating a status column based on the percentage
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK")


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df) # printing the dataframe as it is
print()

not_ok = df[df["status"] != "OK"] # filtering to keep only the rows with a status that is not 'OK'
print(not_ok)
print()

grouped = df.groupby("status") # grouping the data by status
print(grouped["status"].value_counts()) # printing the counts per status
print()

df.to_csv("new_file.csv", index=False) # saving the full dataframe to a new file

import matplotlib.pyplot as plt

df["status"].value_counts().plot(kind="bar") # creating a bar chart showing status counts
plt.title("Count by status") # aadding a title to the graph
plt.savefig("status_bar_chart.png") # saving the graph as an image


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
