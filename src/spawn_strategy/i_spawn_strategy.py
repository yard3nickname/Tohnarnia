import abc

from src.location import Location


class ISpawnStrategy(abc.ABC):
    @abc.abstractmethod
    def get_spawning_location(self) -> Location:
        pass
