from __future__ import annotations

from structlog import get_logger

from ..src.parking_lot import car, parkinglot

logger = get_logger(__name__)


def test_car():
    test_car = car()
    assert test_car.wheels == 4
    assert test_car.size == "small"


def test_parkinglot_set_floors():
    test_parkinglot = parkinglot()
    assert test_parkinglot.garage == {}
    test_parkinglot.set_floors(floors=4)
    assert test_parkinglot.garage[0] == {}
    assert test_parkinglot.garage == {0: {}, 1: {}, 2: {}, 3: {}}


def test_parkinglot_set_floor_spaces():
    test_parkinglot = parkinglot()
    test_parkinglot.set_floors(floors=2)
    test_parkinglot.set_floor_spaces(floor=0, small=2, medium=2, large=2)
    test_parkinglot.set_floor_spaces(floor=1, medium=1, large=1)
    assert test_parkinglot.garage[1][1] == {
        "spot": 1,
        "floor": 1,
        "occupied": False,
        "size": "large",
    }


def test_parkinglot_get_space():
    test_parkinglot = parkinglot()
    test_parkinglot.set_floors(floors=2)
    test_parkinglot.set_floor_spaces(floor=0, small=2, medium=2, large=2)
    test_parkinglot.set_floor_spaces(floor=1, medium=1, large=1)
    available_space = test_parkinglot.get_space()
    assert available_space == {
        "spot": 0,
        "floor": 0,
        "occupied": False,
        "size": "small",
    }
    available_space_large = test_parkinglot.get_space(size="large")
    assert available_space_large == {
        "spot": 4,
        "floor": 0,
        "occupied": False,
        "size": "large",
    }


def test_parkinglot_reserve_space():
    test_parkinglot = parkinglot()
    test_parkinglot.set_floors(floors=2)
    test_parkinglot.set_floor_spaces(floor=0, small=2, medium=2, large=2)
    test_parkinglot.set_floor_spaces(floor=1, medium=1, large=1)
    available_space_large = test_parkinglot.get_space(size="large")
    assert test_parkinglot.reserve_space(spot=available_space_large)


def test_parkinglot_get_space_occupied():
    test_parkinglot = parkinglot()
    test_parkinglot.set_floors(floors=2)
    test_parkinglot.set_floor_spaces(floor=0, small=2, medium=2, large=2)
    test_parkinglot.set_floor_spaces(floor=1, medium=1, large=1)
    space_large = test_parkinglot.get_space(size="large")
    assert test_parkinglot.reserve_space(spot=space_large)
    assert test_parkinglot.get_space(spot=space_large)["occupied"]


def test_parkinglot_get_amount_of_available_spaces():
    test_parkinglot = parkinglot()
    test_parkinglot.set_floors(floors=2)
    test_parkinglot.set_floor_spaces(floor=0, small=2, medium=2, large=2)
    test_parkinglot.set_floor_spaces(floor=1, medium=1, large=1)
    space_large = test_parkinglot.get_space(size="large")
    available_spaces_before_reservation = (
        test_parkinglot.get_amount_of_available_spaces(size="large")
    )
    test_parkinglot.reserve_space(spot=space_large)
    available_spaces_after_reservation = test_parkinglot.get_amount_of_available_spaces(
        size="large"
    )
    assert available_spaces_before_reservation == 3
    assert available_spaces_after_reservation == 2
