from .mapa import Mapa
from .piece_location_mapping import PieceLocationMapping
from .spawner import Spawner
from .navigator import Navigator


class Board:
    def __init__(self, mapa, piece_loc_mapping, spawner, navigator):
        self._mapa = mapa
        self._piece_loc_mapping = piece_loc_mapping
        self._spawner = spawner
        self._navigator = navigator

    def spawn(self, piece, loc):
        pass

