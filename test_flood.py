"""Unit tests for the flood module"""

from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

stations = build_station_list()
update_water_levels(stations)

def test_stations_highest_rel_level():    
    topstations = stations_highest_rel_level(stations, 5)
    prevval = -10000
    for i in topstations:
        assert i[1] > prevval
        prevval = i[1]

def test_stations_level_over_threshold():
    lst = stations_level_over_threshold(stations,0.8)
    for station in lst:
        assert station[1] > 0.8