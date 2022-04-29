"""
This file contains the interpolator function to generate both the series on the same interpolated timeseries
"""

import pandas as pd
import numpy as np


def interpolator(start, end, num, data_series, threshold, values):
    interp_array = np.linspace(start=start, stop=end, num=num)
    return_frame = pd.DataFrame()
    interp_values = []
    for x in interp_array:
        lower_limit = x - threshold
        upper_limit = x + threshold
        sampling_series = data_series[data_series['age_ka'].between(lower_limit, upper_limit)]
        interp_values.append(sampling_series[values].mean())
    return_frame[values] = interp_values
    return_frame["age_ka"] = interp_array
    return return_frame

