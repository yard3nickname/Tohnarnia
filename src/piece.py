from src.spawn_strategy import ISpawnStrategy


class Piece:
    def __init__(self, spawn_strategy: ISpawnStrategy):
        self._spawn_strategy = spawn_strategy
