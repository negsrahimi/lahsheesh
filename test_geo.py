"""Tests for functions defined in the floodsystem/geo module
"""

from floodsystem import geo
from floodsystem.stationdata import build_station_list

stations = build_station_list()

def test_stations_within_radius():
    centre = (52.2053, 0.1218)

    #check that no stations are at a negative distance from the centre
    assert geo.stations_within_radius(stations, centre, 0) == []
    #check that all stations are within 10000km of the centre
    assert len(geo.stations_within_radius(stations, centre, 10000)) == len(stations)

def test_rivers_by_station_number():
    lst = geo.rivers_by_station_number(stations, 2)

    #check that the number of stations is greater (or equal to the second one) for the first river.
    assert lst[0][1] >= lst[1][1]
