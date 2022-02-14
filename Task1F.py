# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""

    #Build station list
    stations = build_station_list()

    inconsistent_stations = inconsistent_typical_range_stations(stations).sort()
    print(inconsistent_stations)
    

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***\n")
    run()
