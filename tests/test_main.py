from __future__ import annotations

from ..main import car


def test_car():
    test_car = car()
    assert test_car.wheels == 4
    assert test_car.size == "small"
