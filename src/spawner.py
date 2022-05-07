from .piece import Piece
from .location import Location
from .piece_location_mapping import PieceLocationMapping


class Spawner:
    def __init__(self, piece_loc_mapping: PieceLocationMapping):
        self.piece_loc_mapping = piece_loc_mapping

    def spawn(self, piece: Piece):
        self.piece_loc_mapping[piece] = piece._spawn_strategy.get_spawning_location()
