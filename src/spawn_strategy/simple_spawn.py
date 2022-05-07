from .i_spawn_strategy import ISpawnStrategy
from ..location import Location


class SimpleSpawn(ISpawnStrategy):
    def __init__(self, loc: Location):
        self._loc = loc

    def get_spawning_loc(self):
        return self._loc
