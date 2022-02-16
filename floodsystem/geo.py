# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqa
#from math import asin, cos, sin, sqrt, pow
from haversine import haversine


def stations_by_distance(stations, p):
    """ This function takes a list of monitoring stations and a coordinate p, and returns a sorted
    list of (station, distance) tuples where distance is the distance of the station from p.
    """
    distances = []
    for station in stations:
        distance = haversine(station.coord, p)
        distances.append((station, distance))
    distances = sorted_by_key(distances, 1)
    return distances

##""" A function to calculate the haversine distance between two coordinates in kilometres.
##"""
##def haversine(c1, c2):
##    r = 6371
##    lat1, long1 = c1
##    lat2, long2 = c2
##
##    part1 = pow(sin((lat2 - lat1)/2), 2)
##    print(part1)
##    part2 = cos(long1) * cos(long2) * pow(sin((long2 - long1)/2), 2)
##    print(part2)
##    
##    distance = 2 * r * asin(sqrt(abs(part1 + part2)))

def rivers_with_station(stations):
    """ Given a list of station objects, this function returns a list of rivers with a monitoring
    station.
    """
    rivers = []
    for station in stations:
        if station.river not in rivers:
            rivers.append(station.river)

    #print(rivers)
    return rivers

def stations_by_river(stations):
    """ Given a list of station objects, this function returns a dictionary that maps river names
    to a list of station objects on a given river.
    """
    mapping = {}
    for station in stations:
        river = station.river
        if river in mapping.keys():
            mapping[river].append(station)
        else:
            mapping[river] = [station]
    return mapping

def stations_within_radius(stations, centre, r):
    """Given a radius r and a geographic coordinate x, this function returns a list of all stations 
    within radius r of a geographic coordinate x"""
    within_radius=[]
    for station in stations:
        if haversine(station.coord, centre)<r:
            within_radius.append(station)
    return within_radius

def rivers_by_station_number(stations, N):
    """Given a number N, determines the N rivers with the greatest number of monitoring stations"""
    stations_river = stations_by_river(stations)
    stations_no = sorted_by_key([(i, len(stations_river[i])) for i in stations_river], 1, reverse=True)

    cutoff = stations_no[N-1][1] 
    stations_no_but_cooler = []
    for i in stations_no:
        if i[1] >= cutoff:
           stations_no_but_cooler.append(i)
    return stations_no_but_cooler
