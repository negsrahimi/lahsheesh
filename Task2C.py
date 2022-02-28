# Demonstration program for Task2C

from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    #print(stations)
    lst = stations_highest_rel_level(stations, 10)
    #print(lst)

    for station in lst:
        print(station.name + '  ' + str(station.relative_water_level()))

if __name__ == "__main__":
    run()
