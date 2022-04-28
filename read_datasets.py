import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

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

# plot the results
fig, ax = plt.subplots()

ax.plot(xrf_980.age_ka, xrf_980.Zr_Sr, 'r')
ax.plot(xrf_981.age_ka, xrf_981.Zr_Sr, 'b')

ax.set_xlim([0, 2250])

plt.show()


