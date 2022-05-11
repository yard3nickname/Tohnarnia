from src.spawn_strategy import ISpawnStrategy

from src.location import Location
from src.mapa import Mapa
from src.piece_location_mapping import PieceLocationMapping

from random import choice


class RandomSpawn(ISpawnStrategy):
    def __init__(self, mapa: Mapa, piece_loc_mapping: PieceLocationMapping):
        self._mapa = mapa
        self._piece_loc_mapping = piece_loc_mapping

    def get_spawning_location(self) -> Location:
        # more work should be done here! good only for first level
        filter_function = lambda loc: loc not in [Location(0, 0)]
        return choice(list(filter(filter_function, self._mapa.get_locations())))
