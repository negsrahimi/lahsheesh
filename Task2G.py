# Demonstration program for Task2G

from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.analysis import future_rel_level
from floodsystem.flood import stations_level_over_threshold

def risk_ranking(stations):
    lst = []
    dt = 3
    p = 4
    future = 0.5
    for station in stations:
        #print(station.name)
        if station.name != 'Letcombe Bassett':
            frl = future_rel_level(station, dt, p, future)
        else:
            frl = 623.4567828
        if frl > 2:
            threat = "severe"
        elif frl > 1.5:
            threat = "high"
        elif frl > 1:
            threat = "moderate"
        else:
            threat = "low"
        lst.append((station.town, frl, threat))
    lst = sorted_by_key(lst, 1, reverse=True)
    town_list = [x[0] for x in lst]

    n = len(lst)
    for i in range(n-1, 0, -1):
        if town_list[i] in town_list[:i]:
            lst = lst[:i] + lst[i+1:]
            town_list = town_list[:i] + town_list[i+1:]
    return lst
        

def run():
    tol = 0.8
    stations = [x[0] for x in stations_level_over_threshold(build_station_list(), tol)]
    towns = risk_ranking(stations)[:60]
    for town in towns:
        if town[0] != None:
            print(town[0], town[1], town[2], sep = '  ')

if __name__ == "__main__":
    run()
