from src.piece_location_mapping import PieceLocationMapping
from src.piece import Piece
from src.spawn_strategy import ISpawnStrategy


class Spawner:
    def __init__(self, piece_loc_mapping: PieceLocationMapping):
        self.piece_loc_mapping = piece_loc_mapping

    def spawn(self, piece: Piece, spawn_strategy: ISpawnStrategy):
        self.piece_loc_mapping.add_piece_mapping(piece, spawn_strategy)
