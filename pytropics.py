__author__ = 'David'

from game import *

screen_size = width, height = 256, 240
black = 0, 0, 0
tile_size = 16

if __name__ == "__main__":
    pygame.init()

    game = Game()
    game.run()