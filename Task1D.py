# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """Requirements for Task 1D"""

    #Build station list and mapping.
    stations = build_station_list()
    mapping = stations_by_river()

    rivers = rivers_with_station(stations).sort()
    print(len(rivers) + 'rivers.')
    print('First 10 - ' + rivers[:10])

    for riv in ['River Aire', 'River Cam', 'River Thames']:
        sta = mapping[riv].sort()
        print(sta)
    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***\n")
    run()
