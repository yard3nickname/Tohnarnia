from .game import Game


class Bootstrapper:
    def __init__(self):
        pass

    def boot(self):
        game = Game()
        game.run()
