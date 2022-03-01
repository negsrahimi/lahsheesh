# A module with plotting functions

import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import time
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    """displays a plot of the water level data against time for a station;
       includes lines for the typical low and high levels."""
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(y=station.typical_range[0], color='b', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """This function plots the water level data and the best-fit polynomial for the given station.
    """
    # Plot
    plt.plot(dates, levels)
    poly, d0 = polyfit(dates, levels, p)

    dates = date2num(dates)
    x1 = np.linspace(dates[0], dates[-1], 300)
    plt.plot(x1, poly(x1 - d0))

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(y=station.typical_range[0], color='b', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
