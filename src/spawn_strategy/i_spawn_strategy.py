from ..location import Location


class ISpawnStrategy:
    def get_spawning_location(self) -> Location:
        pass
