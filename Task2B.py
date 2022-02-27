# Demonstration file for Task2B

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    tol = 0.8
    lst = stations_level_over_threshold(stations, tol)

    for x in lst:
        print(x[0] + '  ' + str(x[1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
