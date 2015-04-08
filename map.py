__author__ = 'David'

import re
import pytmx, pyscroll

from pytropics import *


walkable_tiles = ["Stair.*", "Grass.*", "Pit.*"]

def screen_to_tile_coords(screen_x, screen_y):
    return screen_x // 16, screen_y // 16

class Map(object):
    def __init__(self, tile_map):
        self.map = pytmx.load_pygame(tile_map)
        self.data = pyscroll.TiledMapData(self.map)
        self.layer = pyscroll.BufferedRenderer(self.data, screen_size)

        self.rooms = list()
        room_data = open("resources/Dungeon1_Rooms.txt", "r")

        for entry in room_data:
            entry_data = entry.split(",")
            self.rooms.append(Room(int(entry_data[0]), int(entry_data[1]), int(entry_data[2]), int(entry_data[3]),
                                   int(entry_data[4]), int(entry_data[5]), int(entry_data[6]), int(entry_data[7])))

        self.current_room = self.rooms[0]

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


class Room(object):
    def __init__(self, x, y, room_width, room_height, cam_min_x, cam_max_x, cam_min_y, cam_max_y):
        self.x = x
        self.y = y

        self.width = room_width
        self.height = room_height

        self.cam_min_x = cam_min_x
        self.cam_max_x = cam_max_x
        self.cam_min_y = cam_min_y
        self.cam_max_y = cam_max_y
