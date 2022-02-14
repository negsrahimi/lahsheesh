# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from math import asin, cos, sin, sqrt, pow

""" This function takes a list of monitoring stations and a coordinate p, and returns a sorted
list of (station, distance) tuples where distance is the distance of the station from p.
"""
def stations_by_distance(stations, p):
    distances = []
    for station in stations:
        distance = haversine(station.coordinate, p)
        distances.append((station, distance))
    distances = sorted_by_key(distances)
    return distances

""" A function to calculate the haversine distance between two coordinates in kilometres.
"""
def haversine(c1, c2):
    r = 6371
    lat1, long1 = c1
    lat2, long2 = c2

    part1 = pow(sin((lat2 - lat1)/2), 2)
    part2 = cos(long1) * cos(long2) * pow(sin((long2 - long1)/2), 2)
    
    distance = 2 * r * asin(sqrt(part1 + part2))
