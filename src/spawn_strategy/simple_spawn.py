from src.spawn_strategy import ISpawnStrategy
from src.location import Location


class SimpleSpawn(ISpawnStrategy):
    def __init__(self, loc: Location):
        self._loc = loc

    def get_spawning_location(self) -> Location:
        return self._loc
