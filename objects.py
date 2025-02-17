import pygame
from settings import *


class Object:
    def __init__(self, x, y, texture_paths, angle=0):
        self.x = x
        self.y = y
        self.textures = [pygame.image.load(path) for path in texture_paths]
        self.num_textures = len(self.textures)
        self.angle = angle
        self.texture_width = self.textures[0].get_width()
        self.texture_height = self.textures[0].get_height()

    def draw(self, screen, depth, screen_x, player_x, player_y):
        proj_height = PROJ_COEFF / depth

        view_angle = math.atan2(player_y - self.y, player_x - self.x)
        relative_angle = (view_angle - self.angle) % (2 * math.pi)

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


class Enemy(Object):
    def __init__(self, x, y, texture_paths, angle=0, speed=PLAYER_SPEED):
        super().__init__(x, y, texture_paths, angle)
        self.speed = speed / FPS

    def movement(self, player):
        x, y, _ = player.pos()
        ray_angle = math.atan2(y - self.y, x - self.x)
        ray_angle = (ray_angle + 2 * math.pi) % (2 * math.pi)

        delta_angle = (ray_angle - self.angle + math.pi) % (2 * math.pi) - math.pi

        self.angle += delta_angle

        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed


class Barrel(Object):
    def __init__(self, x, y):
        texture_paths = ['data/textures/objects/barrel/barrel.png']
        super().__init__(x, y, texture_paths)


class Devil(Enemy):
    def __init__(self, x, y, angle=0, speed=PLAYER_SPEED):
        texture_paths = [f'data/textures/objects/devil/{i}.png' for i in range(8)]
        super().__init__(x, y, texture_paths, angle, speed)


class Ghost(Enemy):
    def __init__(self, x, y, angle=0, speed=PLAYER_SPEED):
        texture_paths = ['data/textures/objects/ghost/ghost.png']
        super().__init__(x, y, texture_paths, angle, speed)


objects = [
    Barrel(5, 5),
    Barrel(3, 4),
    Devil(21, 10, speed=1.5),
    Barrel(22, 2),
    Devil(1.5, 9.5, speed=1.5),
    Ghost(21, 5, speed=PLAYER_RUNNING_SPEED)
]
