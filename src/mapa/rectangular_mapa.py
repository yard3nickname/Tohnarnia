from src.mapa import Mapa
from src.location import Location


class RectangularMapa(Mapa):
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns

    def get_locations(self) -> list[Location]:
        return [Location(row, column) for row in range(self._rows) for column in range(self._columns)]

    def get_valid_location(self, loc: Location) -> Location:
        return Location(loc._row % self._rows, loc._column % self._columns)
