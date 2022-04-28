"""
This script will load the FileNames from the SQL databases and convert them to IDs as you would find in a normal
dataset, so they can be used in the future.

"""

import sqlite3
import pandas as pd


# load the SQL database
connection = sqlite3.connect("data/xrf_data.db")
xrf_980 = pd.read_sql("SELECT * FROM xrf_980", connection)

xrf_980["ID"] = xrf_980.FileName.str.split("\\")[5]

print(xrf_980.ID.head())


