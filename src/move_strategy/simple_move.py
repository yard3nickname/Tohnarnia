from src.move_strategy.i_move_strategy import IMoveStrategy

from src.relative_location import RelativeLocation


class SimpleMove(IMoveStrategy):
    def get_optional_locations(self, current_location, speed):
        return [
            current_location + RelativeLocation(1, 0) * speed,
            current_location + RelativeLocation(0, 1) * speed,
            current_location - RelativeLocation(1, 0) * speed,
            current_location - RelativeLocation(0, 1) * speed,
        ]
