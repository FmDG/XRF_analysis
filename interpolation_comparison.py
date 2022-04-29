"""
To compare the IRD data and the XRF data it is necessary to interpolate the two plots to the same sampling frequency.
"""

import pandas as pd
import sqlite3
from interpolator import interpolator
import matplotlib.pyplot as plt

# connect to the SQL databases containing the XRF data
connection_01 = sqlite3.connect("data/xrf_data.db")
# connect to the IRD database to load data
connection_02 = sqlite3.connect("data/ird_data.db")

# read the SQL databases into a Pandas dataframe
ird = pd.read_sql("SELECT * FROM ird", connection_02)
xrf_980 = pd.read_sql("SELECT * FROM xrf_980", connection_01)
xrf_981 = pd.read_sql("SELECT * FROM xrf_981", connection_01)

# close connection to SQL databases
connection_01.close()
connection_02.close()


xrf_interp = interpolator(0, 1000, 2000, xrf_980, 0.5, 'Zr_Sr')
ird_interp = interpolator(0, 1000, 2000, ird, 0.5, 'ird_lithics_gm')

fig, axs = plt.subplots(2)

axs[0].plot(xrf_interp.age_ka, xrf_interp.Zr_Sr)
axs[1].plot(ird_interp.age_ka, ird_interp.ird_lithics_gm)

plt.show()
