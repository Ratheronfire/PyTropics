__author__ = 'David'

import pygame
from enum import Enum
from pygame.locals import *

import pytropics
import sprite
import map


class states(Enum):
    title = 1
    overworld = 2
    dungeon = 3
    dialogue = 4

class Game(object):
    def __init__(self):
        self.display = Display(pygame.display.set_mode(pytropics.screen_size), states.dungeon)

        self.map = map.Map("resources/Dungeon1.tmx")

        self.sprite_group = sprite.SpriteGroup(self.map)

        self.player = sprite.Player(["resources/Mike.png"], 29, 168, self.map)
        self.sprite_group.add(self.player)
        self.sprite_group.center(self.player.rect.center)
        self.sprite_group.player_sprite = self.player

        self.last_pressed = pygame.key.get_pressed()

    def run(self):
        clock = pygame.time.Clock()
        fps = 60
        scale = pygame.transform.scale
        self.running = True

        while self.running:
            dt = clock.tick(fps) / 1000

            self.handle_input()
            self.update(dt)

            self.display.start_draw()
            self.display.draw(self.sprite_group)
            self.display.end_draw()

    def handle_input(self):
        events = pygame.event.get()
        pressed = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                exit(0)

        if pressed[K_ESCAPE]:
            self.running = False

        if pressed[K_LEFT] and not self.last_pressed[K_LEFT]:
            self.player.move(self.player.pos[0] - 1, self.player.pos[1])

        if pressed[K_RIGHT] and not self.last_pressed[K_RIGHT]:
            self.player.move(self.player.pos[0] + 1, self.player.pos[1])

        if pressed[K_UP] and not self.last_pressed[K_UP]:
            self.player.move(self.player.pos[0], self.player.pos[1] - 1)

        if pressed[K_DOWN] and not self.last_pressed[K_DOWN]:
            self.player.move(self.player.pos[0], self.player.pos[1] + 1)

        self.last_pressed = pressed

    def update(self, dt):
        self.sprite_group.update(dt)

class Display(object):
    def __init__(self, screen, state):
        self.screen = screen
        self.state = state

    def start_draw(self):
        self.screen.fill(pytropics.black)

    def draw(self, object_to_draw):
        object_to_draw.draw(self.screen)

    def end_draw(self):
        pygame.display.flip()
