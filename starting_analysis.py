"""
This code generates a number of simple graphs which are used for exploratory analysis of the data, both the XRF data
generated and the comparative d18O and IRD data.

"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Set the age (in ka) where the splice will occur between the 980 and 981 datasets
splice_point = 900

# Define the age limits for the plots
lower_age = 0
upper_age = 1000


# Set the style for the plots
sns.set_theme(style="ticks")
pallet = sns.color_palette()

# connect to the SQL databases containing the XRF data
connection = sqlite3.connect("data/xrf_data.db")

# read the SQL databases into a Pandas dataframe
xrf_980 = pd.read_sql("SELECT * FROM xrf_980", connection)
xrf_981 = pd.read_sql("SELECT * FROM xrf_981", connection)

# close connection to SQL databases
connection.close()

# connect to the IRD database to load data
connection = sqlite3.connect("data/ird_data.db")

# read the SQL databases into a Pandas dataframe
ird = pd.read_sql("SELECT * FROM ird", connection)

# close connection to SQL databases
connection.close()


# join the two datasets
xrf_980 = xrf_980[xrf_980.age_ka < splice_point]
xrf_981 = xrf_981[xrf_981.age_ka > splice_point]

# plot up the results
fig, axs = plt.subplots(2)

# Plot the IRD data in subplot 0
axs[0].plot(ird.age_ka, ird.ird_lithics_gm, color=pallet[0])

# Set paramters for plot
axs[0].set(xlim=[lower_age, upper_age], xlabel="Age (ka)", ylabel="IRD (lithics/gm)")


# Plot the XRF data in subplot 1
axs[1].plot(xrf_980.age_ka, xrf_980.Zr_Sr, color=pallet[1])
axs[1].plot(xrf_981.age_ka, xrf_981.Zr_Sr, color=pallet[2])

# Set parameters for plot
axs[1].set(xlim=[lower_age, upper_age], ylim=[0, 1.4], xlabel="Age (ka)", ylabel="Zr/Sr ratio")
axs[1].legend(["980", "981"])

# Show plot
plt.show()
