# Demonstration program for Task2F

from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    stations = build_station_list()
    lst = stations_highest_rel_level(stations, 6)
    dt = 2

    for station in lst:
        if station.name != 'Letcombe Bassett':
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    run()