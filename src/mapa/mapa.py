import abc

from src.location import Location


class Mapa(abc.ABC):
    @abc.abstractmethod
    def get_locations(self) -> list[Location]:
        pass

    @abc.abstractmethod
    def get_valid_location(self, loc: Location) -> Location:
        pass
