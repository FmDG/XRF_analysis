"""
This script will take the ugly raw data from the two SQL datasets and put them in one easy to use SQL database
called xrf_data.db with the tables xrf_980 and xrf_981 containing the two different datasets with Si/Sr ratios, Zr/Sr
ratios, ages relative to LR04 dataset, depth in metres composite depth, and the filename for data-search later.
"""

import pandas as pd
import sqlite3

# connect to the SQL databases containing the XRF data
connection_980 = sqlite3.connect("data/980_data.db")
connection_981 = sqlite3.connect("data/981_data.db")

# read the SQL databases into a Pandas dataframe
xrf_980 = pd.read_sql("SELECT * FROM xrf", connection_980)
xrf_981 = pd.read_sql("SELECT * FROM xrf", connection_981)

# close connection to SQL databases
connection_980.close()
connection_981.close()

# define Zr/Sr as the ratio of the element counts to each other
xrf_980["Zr_Sr"] = xrf_980["Zr_Area "]/xrf_980["Sr_Area "]
xrf_981["Zr_Sr"] = xrf_981["Zr_Area "]/xrf_981["Sr_Area "]

# define Si/Sr as the ratio of the element counts to each other
xrf_980["Si_Sr"] = xrf_980["Si_Area "]/xrf_980["Sr_Area "]
xrf_981["Si_Sr"] = xrf_981["Si_Area "]/xrf_981["Sr_Area "]

# rename the LR04 age column to age
xrf_980 = xrf_980.rename(columns={"age(ka)_lr04": "age_ka"})
xrf_981 = xrf_981.rename(columns={"age(ka)_lr04": "age_ka"})

# create new dataframes
new_980 = xrf_980[["age_ka", "Si_Sr", "Zr_Sr", "mcd", "FileName"]]
new_981 = xrf_981[["age_ka", "Si_Sr", "Zr_Sr", "mcd", "FileName"]]

# Opens an SQL database and puts the data into it - this will speed up future access
conn = sqlite3.connect('data/xrf_data.db')
c = conn.cursor()
# c.execute("DROP TABLE xrf")
c.execute("CREATE TABLE IF NOT EXISTS xrf_980 (Depth number)")
c.execute("CREATE TABLE IF NOT EXISTS xrf_981 (Depth number)")
conn.commit()

# Generates ID column which contains the ID from the filename
new_980["id"] = (new_980.FileName.str.split(pat="\\", n=5)).apply(pd.Series)[4]
new_980["id"] = (new_980.FileName.str.split(pat="\\", n=5)).apply(pd.Series)[4]

# Writes the new dataframes to the database
new_980.to_sql('xrf_980', conn, if_exists='replace')
new_981.to_sql('xrf_981', conn, if_exists='replace')

# Commits changes and closes connection
conn.commit()

conn.close()

