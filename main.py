from __future__ import annotations


class automobile:
    wheels = 4
    seats = 4
    size = "medium"


class car(automobile):
    def __init__(self):
        super().__init__()
        self.size = "small"


def main():
    return car()
