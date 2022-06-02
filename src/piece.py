from src.move_strategy import IMoveStrategy


class Piece:
    def __init__(self, move_strategy: IMoveStrategy):
        self._move_strategy = move_strategy