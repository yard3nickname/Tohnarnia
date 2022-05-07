from .piece import Piece
from .location import Location


class PieceLocationMapping:
    def __init__(self):
        self.mapping = dict()

    def add_piece_mapping(self, piece: Piece, loc: Location):
        self.mapping[piece] = loc

    def remove_piece_mapping(self, piece: Piece):
        del self.mapping[piece]

    def get_piece_location(self, piece) -> Location:
        return self.mapping[piece]

    def get_pieces_by_location(self, loc) -> list[Piece]:
        return [k for k, v in self.mapping if v == loc]
