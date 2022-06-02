from dataclasses import dataclass

from src.piece_location_mapping import PieceLocationMapping
from src.spawner import Spawner
from src.mapa import RectangularMapa

from src.character import Character
from src.spawn_strategy import SimpleSpawn
from src.spawn_strategy import RandomSpawn
from src.location import Location

from src.action import move


@dataclass
class Game:
    # turn: int = 0
    # board: Board
    # plmap: PieceLocationMap
    # spawner: Spawner
    # mover: Mover
    # pieces: list[Piece]

    def init(self):
        for piece in self.pieces:
            self.spawner.spawn(piece, )

    def run(self):
        m = move.Up()
        print(m.move(Location(0, 0), 3))
        print(m.__class__.__name__)
        # print(SimpleSpawn(Location(0, 0)).get_spawning_location())
        # ch1 = Character(SimpleSpawn(Location(0, 0)), 'Hero', 2)
        # ch2 = Character(RandomSpawn(self._mapa, self.piece_loc_mapping), 'BBEG', 1)
        # self.spawner.spawn(ch1)
        # self.spawner.spawn(ch2)
        # print(self.piece_loc_mapping._mapping)
        # print(self.piece_loc_mapping.get_piece_location(ch1))
