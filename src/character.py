from .piece import Piece


class Character(Piece):
    def __init__(self, spawn_strategy, name, speed):
        super.__init__(spawn_strategy)
        self._name = name
        self._speed = speed

