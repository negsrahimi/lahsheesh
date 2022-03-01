from floodsystem.analysis import future_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()

def test_future_rel_level():
    dt = 3
    p = 4
    future = 1
    station = stations[10]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    assert future_rel_level(station, dt, p, future) > 0

