# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Print list of stations within 10km of the Cambridge city centre in alphabetical order
    centre = (52.2053, 0.1218)
    the_list = stations_within_radius(stations, centre, 10)
    print(sorted([i.name for i in the_list]))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
