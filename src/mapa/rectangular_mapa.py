from .mapa import Mapa

from ..location import Location


class RectangularMapa(Mapa):
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns

    def get_locations(self) -> list[Location]:
        return [Location(row, column) for row in self._rows for column in self._columns]

    def get_valid_location(self, loc: Location) -> Location:
        return Location(loc._row % self._rows, loc._column % self._columns)
