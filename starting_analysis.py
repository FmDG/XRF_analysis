import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Set the age (in ka) where the splice will occur between the 980 and 981 datasets
splice_point = 900

# Set the style for the plots
sns.set_theme(style="ticks")

# connect to the SQL databases containing the XRF data
connection = sqlite3.connect("data/xrf_data.db")

# read the SQL databases into a Pandas dataframe
xrf_980 = pd.read_sql("SELECT * FROM xrf_980", connection)
xrf_981 = pd.read_sql("SELECT * FROM xrf_981", connection)

# close connection to SQL databases
connection.close()

# join the two datasets
xrf_980 = xrf_980[xrf_980.age_ka < splice_point]
xrf_981 = xrf_981[xrf_981.age_ka > splice_point]

# plot up the results
fig, ax = plt.subplots()

ax.plot(xrf_980.age_ka, xrf_980.Zr_Sr)
ax.plot(xrf_981.age_ka, xrf_981.Zr_Sr)

ax.set(xlim=[0, 2250], ylim=[0, 1.4], xlabel="Age (ka)", ylabel="Zr/Sr ratio")
ax.legend(["980", "981"])

plt.show()
