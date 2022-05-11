from src.piece import Piece
from src.location import Location


class PieceLocationMapping:
    def __init__(self):
        self._mapping = dict()

    def add_piece_mapping(self, piece: Piece, loc: Location):
        self._mapping[piece] = loc

    def remove_piece_mapping(self, piece: Piece):
        del self._mapping[piece]

    def get_piece_location(self, piece) -> Location:
        return self._mapping[piece]

    def get_pieces_by_location(self, loc) -> list[Piece]:
        return [k for k, v in self._mapping if v == loc]
