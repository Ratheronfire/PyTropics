__author__ = 'David'

import sys, pygame, pytmx, pyscroll
from pygame.locals import *
from pytropics import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, images, tile_x, tile_y, map):
        pygame.sprite.Sprite.__init__(self)
        self.group = pyscroll.PyscrollGroup
        self.map = map

        self.speed = 200

        sprites = dict()
        for image in images:
            sprites[image] = pygame.image.load(image)

        # the first sprite is used as the default
        self.image = sprites[images[0]]

        self.pos = (tile_x, tile_y + 1)
        self.dx = self.dy = 0
        self.moving = False

        self.rect = self.image.get_rect()
        self.rect.x = tile_x * tile_size
        self.rect.y = tile_y * tile_size

    def set_group(self, group):
        self.group = group

    def set_sprite(self, image):
        self.image = self.sprites[image]

    def move(self, x, y):
        if not self.moving and self.map.is_walkable(x, y):
            self.dx = x - self.pos[0]
            self.dy = y - self.pos[1]
            self.moving = True

    def update(self, dt):
        self.rect.x += self.dx * self.speed * dt
        self.rect.y += self.dy * self.speed * dt

        if self.moving and ((self.dx < 0 and self.rect.x < (self.pos[0] - 1) * tile_size) or
                                (self.dx > 0 and self.rect.x > (self.pos[0] + 1) * tile_size)):
            self.pos = (self.pos[0] + self.dx, self.pos[1])
            self.rect.x = self.pos[0] * tile_size
            self.dx = 0
            self.moving = False

        if self.moving and ((self.dy < 0 and self.rect.y < (self.pos[1] - 2) * tile_size) or
                                (self.dy > 0 and self.rect.y > (self.pos[1]) * tile_size)):
            self.pos = (self.pos[0], self.pos[1] + self.dy)
            self.rect.y = (self.pos[1] - 1) * tile_size
            self.dy = 0
            self.moving = False

class SpriteGroup(pyscroll.PyscrollGroup):
    def __init__(self, map_layer):
        pyscroll.PyscrollGroup.__init__(self, map_layer=map_layer)

    def add_sprite(self, sprite):
        self.add(sprite)

        sprite.set_group(self)

    def center(self, point):
        pyscroll.PyscrollGroup.center(self, point)

    def update(self, dt):
        pyscroll.PyscrollGroup.update(self, dt)

class Player(Sprite):
    def __init__(self, images, tile_x, tile_y, map):
        Sprite.__init__(self, images, tile_x, tile_y, map)

class Enemy(Sprite):
    def __init__(self, images, tile_x, tile_y, map):
        Sprite.__init__(self, images, tile_x, tile_y, map)

class Item(Sprite):
    def __init__(self, images, tile_x, tile_y, map):
        Sprite.__init__(self, images, tile_x, tile_y, map)

class Door(Sprite):
    def __init__(self, images, tile_x, tile_y, map):
        Sprite.__init__(self, images, tile_x, tile_y, map)

class Switch(Sprite):
    def __init__(self, images, tile_x, tile_y, map):
        Sprite.__init__(self, images, tile_x, tile_y, map)
