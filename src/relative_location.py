class RelativeLocation:
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def __repr__(self):
        return f'RelativeLocation(row: {self._row}, column: {self._column})'

    def __mul__(self, other: int):
        return RelativeLocation(self._row * other, self._column * other)
