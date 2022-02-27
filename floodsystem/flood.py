# A module with functions related to flooding

from utils import sorted_by_key

def stations_in_desc_order(stations):
    lst = []
    for station in stations:
        level = station.relative_water_level()
        if level != None:
            lst.append((station, level))
    return sorted_by_key(lst, 1, reverse=True)

def stations_level_over_threshold(stations, tol):
    """This function takes a list of stations and a tolerance value. It returns a list of tuples, where each tuple holds (i) a station (object) at which the latest
       relative water level is over the tolerance and (ii) the relative water level at the station. The returned list is sorted by the relative level in descending order."""

    lst = stations_in_desc_order(stations)
    n = len(lst)
    for i in range(n):
        if lst[n][1] <= tol:
            return lst[:n]


def stations_highest_rel_level(stations, N):
    """returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest (sorted in descending order by relative level)."""

    lst = stations_in_desc_order(stations)[:N]
    return [x[0] for x in lst]
