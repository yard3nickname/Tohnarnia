from dataclasses import dataclass

from src.relative_location import RelativeLocation

from .move import Move


@dataclass
class Down(Move):
    direction: RelativeLocation = RelativeLocation(0, -1)
