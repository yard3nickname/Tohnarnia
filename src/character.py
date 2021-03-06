from .piece import Piece


class Character(Piece):
    def __init__(self, move_strategy, name, speed):
        super().__init__(move_strategy)
        self._name = name
        self._speed = speed

    def __repr__(self):
        return f'Character(\'{self._name}\')'
