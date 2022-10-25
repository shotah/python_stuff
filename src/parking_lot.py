from __future__ import annotations

from structlog import get_logger

logger = get_logger(__name__)


class automobile:
    wheels = 4
    seats = 4
    size = "medium"


class car(automobile):
    def __init__(self):
        super().__init__()
        self.size = "small"


class parkinglot:
    def __init__(self) -> None:
        self.garage = {}

    def get_space(self, spot: dict = {}, size: str = "small") -> dict:
        if not spot:
            return self.get_empty_space(size=size)
        return self.garage[spot["floor"]][spot["spot"]]

    def __check_space_is_empty(self, *, floor: int, space: dict, size: str) -> bool:
        if not size:
            return self.garage[floor][space]["occupied"] is False
        return (
            self.garage[floor][space]["occupied"] is False
            and self.garage[floor][space]["size"] == size
        )

    def get_empty_space(self, *, size: str) -> dict:
        for floor in self.garage.keys():
            for space in self.garage[floor]:
                if self.__check_space_is_empty(floor=floor, space=space, size=size):
                    return self.garage[floor][space]
        return {}

    def get_amount_of_available_spaces(self, *, size: str = "") -> int:
        amount_of_spaces = 0
        for floor in self.garage.keys():
            for space in self.garage[floor]:
                if self.__check_space_is_empty(floor=floor, space=space, size=size):
                    amount_of_spaces += 1
        return amount_of_spaces

    def reserve_space(self, spot: dict) -> bool:
        if not spot:
            return False
        self.garage[spot["floor"]][spot["spot"]]["occupied"] = True
        return self.garage[spot["floor"]][spot["spot"]]["occupied"]

    def set_floors(self, *, floors: int) -> None:
        if not floors:
            self.garage = {0: {}}
        self.garage = {floor: {} for floor in range(floors)}

    def __set_floor_space(
        self, spot_num: int = 0, floor: int = 0, size: dict = {}
    ) -> int:
        if not size:
            return spot_num
        for size, qty in size.items():
            for _ in range(qty):
                self.garage[floor][spot_num] = {
                    "spot": spot_num,
                    "occupied": False,
                    "size": size,
                    "floor": floor,
                }
                spot_num += 1
        return spot_num

    def set_floor_spaces(
        self, *, floor: int = 0, small: int = 0, medium: int = 0, large: int = 0
    ) -> None:
        spot_num = 0
        for size in [{"small": small}, {"medium": medium}, {"large": large}]:
            spot_num = self.__set_floor_space(spot_num=spot_num, floor=floor, size=size)
