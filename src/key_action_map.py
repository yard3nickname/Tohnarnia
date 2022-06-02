from dataclasses import dataclass
from src.action import move

@dataclass
class KeyActionMap:
    kamap = {
        'w': move.Up,
        's': move.Down,
        'd': move.Right,
        'a': move.Left,
    }

    def get_action_by_key(self, key):
        if key in self.kamap:
            return self.kamap[key]
        else:
            raise KeyError(key)
