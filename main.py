__author__ = 'David'

import sys, pygame, pytmx, pyscroll
from pygame.locals import *


class Mike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mike.png")
        self.velocity = [0, 0]

        self.rect = self.image.get_rect()
        self.rect.x = 28 * 16
        self.rect.y = 160 * 16

    def update(self, dt):
        self.rect.x += self.velocity[0] * dt
        self.rect.y += self.velocity[1] * dt

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(size)

        dungeon_1_map = pytmx.load_pygame("Dungeon1.tmx")
        dungeon_1_data = pyscroll.TiledMapData(dungeon_1_map)
        dungeon_1_layer = pyscroll.BufferedRenderer(dungeon_1_data, size)

        self.mike_sprite = Mike()

        self.group = pyscroll.PyscrollGroup(map_layer=dungeon_1_layer)
        self.group.add(self.mike_sprite)
        self.group.center(self.mike_sprite.rect.center)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pressed = pygame.key.get_pressed()

        if pressed[K_ESCAPE]:
            self.running = False

        if pressed[K_UP]:
            self.mike_sprite.velocity[1] = -200
        elif pressed[K_DOWN]:
            self.mike_sprite.velocity[1] = 200
        else:
            self.mike_sprite.velocity[1] = 0

        if pressed[K_LEFT]:
            self.mike_sprite.velocity[0] = -200
        elif pressed[K_RIGHT]:
            self.mike_sprite.velocity[0] = 200
        else:
            self.mike_sprite.velocity[0] = 0

    def update(self, dt):
        self.group.update(dt)


    def run(self):
        clock = pygame.time.Clock()
        fps = 60
        scale = pygame.transform.scale
        self.running = True

        while self.running:
            dt = clock.tick(fps) / 1000

            self.handle_input()
            self.update(dt)

            self.group.center(self.mike_sprite.rect.center)

            self.screen.fill(black)
            self.group.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    size = width, height = 256, 240
    black = 0, 0, 0

    game = Game()
    game.run()
