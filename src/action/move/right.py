from dataclasses import dataclass

from src.relative_location import RelativeLocation

from .move import Move


@dataclass
class Right(Move):
    direction: RelativeLocation = RelativeLocation(1, 0)
