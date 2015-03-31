__author__ = 'David'

import sys, pygame, pytmx, pyscroll, re
from pygame.locals import *
from pytropics import *

walkable_tiles = ["Stair.*", "Grass.*", "Pit.*"]

def screen_to_tile_coords(screen_x, screen_y):
    return screen_x // 16, screen_y // 16

class Map(object):
    def __init__(self, tile_map):
        self.map = pytmx.load_pygame(tile_map)
        self.data = pyscroll.TiledMapData(self.map)
        self.layer = pyscroll.BufferedRenderer(self.data, screen_size)

    def is_walkable(self, x, y):
        if x < 0 or x > self.map.width or y < 0 or y > self.map.height:
            return False

        next_tile = self.get_tile_type(x, y)

        for tile in walkable_tiles:
            if re.match(tile, next_tile):
                return True

        return False

    def get_tile_properties(self, x, y, layer=0):
        return self.map.get_tile_properties(x, y, layer)

    def get_tile_type(self, x, y):
        return self.get_tile_properties(x, y)["Type"]

class Overword(Map):
    def __init__(self, tile_map):
        Map.__init__(self, tile_map)

class Dungeon(Map):
    def __init__(self, tile_map):
        Map.__init__(self, tile_map)
