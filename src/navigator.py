from .mapa import Mapa


class Navigator:
    def __init__(self, mapa: Mapa):
        self._mapa = mapa
        # user choice generator in game not to add to here

    def navigate(self, piece, something_about_user_choice):


    # hitlabtut - lo zarich lihiot kan
    def get_right_loc(self, loc):
        loc._column += 1
        return self._get_loc(loc)

    def get_left_loc(self, loc):
        loc._column -= 1
        return self._get_loc(loc)

    def get_up_loc(self, loc):
        loc._row += 1
        return self._get_loc(loc)

    def get_down_loc(self, loc):
        loc._row -= 1
        return self._get_loc(loc)
    # sof hitlabtut