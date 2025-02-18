import pygame
from settings import *


class Object:
    def __init__(self, x, y, texture_paths, angle=0):
        self.x = x
        self.y = y
        self.textures = [pygame.image.load(path) for path in texture_paths]
        self.num_textures = len(self.textures)
        self.texture_width = self.textures[0].get_width()
        self.texture_height = self.textures[0].get_height()
        self.obj_angle = angle

    def draw(self, screen, depth, screen_x, player_x, player_y):
        proj_height = PROJ_COEFF / depth

        view_angle = math.atan2(player_y - self.y, player_x - self.x)
        relative_angle = (view_angle - self.obj_angle) % (2 * math.pi)

        angle_step = 2 * math.pi / self.num_textures
        texture_index = int(relative_angle // angle_step) % self.num_textures

        scaled_texture = pygame.transform.scale(
            self.textures[texture_index],
            (self.texture_width * (proj_height / self.texture_height), proj_height)
        )

        screen.blit(
            scaled_texture, (screen_x - scaled_texture.get_width() / 2, HEIGHT / 2 - proj_height / 2)
        )

    def pos(self):
        return self.x, self.y


class Barrel(Object):
    def __init__(self, x, y, angle=0):
        texture_paths = [f'data/textures/objects/barrel/barrel.png']
        super().__init__(x, y, texture_paths, angle)


class Devil(Object):
    def __init__(self, x, y, angle=0):
        texture_paths = [f'data/textures/objects/devil/{i}.png' for i in range(8)]
        super().__init__(x, y, texture_paths, angle)


objects = [
    Barrel(5, 5),
    Barrel(3, 4),
    Devil(21, 10, 1.87),
    Barrel(22, 2),
    Devil(1.5, 9.5)
]