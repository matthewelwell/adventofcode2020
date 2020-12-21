from utils.day13.bus import Bus


def test_bus_timetable():
    bus = Bus(192)

    assert bus.departure_times(from_=3000)
