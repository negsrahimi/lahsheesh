# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Prints rivers with the value N=9
    stations_no = rivers_by_station_number(stations, 9)
    print(stations_no)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
