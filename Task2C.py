# Demonstration program for Task2C

from floodsystem.stationdata import build_station_data
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_data()
    lst = stations_highest_rel_level(stations, 10)

    for station in lst:
        print(station.name + '' + station.relative_water_level())
