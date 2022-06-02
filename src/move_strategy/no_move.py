from src.move_strategy.i_move_strategy import IMoveStrategy


class NoMove(IMoveStrategy):
    def get_optional_moves(self):
        return []
