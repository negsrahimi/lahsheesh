# A set of functions to analyse water level data

from matplotlib.dates import date2num
import numpy as np
from .datafetcher import fetch_measure_levels
import datetime

def polyfit(dates, levels, p):
    """A function that given the water level time history (dates, levels) for a station computes a least-squares fit of a polynomial of degree p to water level data.
       The function returns a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis.
    """
    dates = date2num(dates)
    #print(dates)
    dates = np.array(dates)
    x = dates[0]
    p_coeff = np.polyfit(dates - x, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, x

def future_rel_level(station, dt, p, future):
    try:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    except KeyError:
        return 0
    if dates != []:
        poly, d0 = polyfit(dates, levels, p)
        dates = date2num(dates)
        future_level = poly(dates[-1] + future - d0)
        if station.typical_range_consistent():
            return (future_level - station.typical_range[0])/(station.typical_range[1] - station.typical_range[0])
    return 0
