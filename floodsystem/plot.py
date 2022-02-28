# A module with plotting functions

import matplotlib.pyplot as plt
import time

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
    time.sleep(3)
    plt.close('all')
