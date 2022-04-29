# XRF_analysis
Data processing for XRF analysis project

## Data

The data is kept as SQL databases because this is quicker to load than any csv or MS Excel files and so allows for ease 
of access. This uses the SQLite3 library built into Python which is pretty intuitive but there is a code attached 
(to_csv_data.py) which is able to convert the data into csv files if this is more convenient.

The IRD data comes from two source cited below:

Wright, AK; Flower, BP (2002): Surface and deep ocean circulation in the subpolar North Atlantic during the 
mid-Pleistocene revolution. Paleoceanography, 17(4), 1068, doi: [10.1029/2002PA000782](https://doi.org/10.1029/2002PA000782)

McManus, J.F., Oppo, D.W., and Cullen, J.L. (2001), 
ODP 980 Isotope and IRD Data, 
IGBP PAGES/World Data Center A for Paleoclimatology 
Data Contribution Series #2001-065. 
NOAA/NGDC Paleoclimatology Program, Boulder CO, USA.

## Starting Analysis

This code contains some simple plotting procedures and is not massively interesting going forward.