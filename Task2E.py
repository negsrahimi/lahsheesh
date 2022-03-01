from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt
import time

def run():
    stations = build_station_list()
    #print(stations)
    lst = stations_highest_rel_level(stations, 6)
    #print(lst)
    dt = 10

    for station in lst:
        if station.name != 'Letcombe Bassett':
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    run()
    
    
    
