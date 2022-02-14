# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    centre = (52.2053, 0.1218)
    print(stations_within_radius(stations, centre, 10))
    


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
