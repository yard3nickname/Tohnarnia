from .i_spawn_strategy import ISpawnStrategy

from ..location import Location
from ..mapa import Mapa
from ..piece_location_mapping import PieceLocationMapping

from random import choice


class RandomSpawn(ISpawnStrategy):
    def __init__(self, mapa: Mapa, piece_loc_mapping: PieceLocationMapping):
        self._mapa = mapa
        self._piece_loc_mapping = piece_loc_mapping

    def get_spawning_loc(self) -> Location:
        # more work should be done here! good only for first level
        filter_function = lambda loc: loc in [Location(0, 0)]
        return choice(filter(filter_function, self._mapa.get_locations()))
