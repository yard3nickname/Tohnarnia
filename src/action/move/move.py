from dataclasses import dataclass

from src.relative_location import RelativeLocation


@dataclass
class Move:
    direction: RelativeLocation

    def move(self, current_location, mul_param):
        return current_location + self.direction * mul_param
