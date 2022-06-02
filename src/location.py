from src.relative_location import RelativeLocation


class Location:
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def __repr__(self):
        return f'Location(row: {self._row}, column: {self._column})'

    def __eq__(self, other):
        return isinstance(other, Location) and self._row == other._row and self._column == other._column

    def __add__(self, other: RelativeLocation):
        return Location(self._row + other._row, self._column + other._column)

    def __sub__(self, other):
        return Location(self._row - other._row, self._column - other._column)
