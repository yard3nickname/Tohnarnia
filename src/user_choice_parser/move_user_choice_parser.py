from .i_user_choice_parser import IUserChoiceParser


class MoveUserChoiceParser(IUserChoiceParser):
    def parse_user_choice(self, user_choice):
        match user_choice:
            case['w']:
                pass
            case['s']:
                pass
            case['a']:
                pass
            case['d']:
                pass
            case _:
                pass
