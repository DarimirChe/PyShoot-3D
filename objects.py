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
    def __init__(self, x, y, texture_paths, damage, health, reload_time, angle=0, speed=PLAYER_SPEED):
        super().__init__(x, y, texture_paths, angle)
        self.speed = speed / FPS
        self.damage = damage
        self.health = health
        self.reload_time = reload_time
        self.frame = reload_time / FPS
        self.frame_count = 0
        self.is_alive = True
        self.size = self.texture_width / 256
        self.animation_time = 1
        self.delta_frame = self.num_textures / (self.animation_time * FPS)
        self.current_frame = 0

    def movement(self, player):
        p_x, p_y, _ = player.pos()
        ray_angle = math.atan2(p_y - self.y, p_x - self.x)
        ray_angle = (ray_angle + 2 * math.pi) % (2 * math.pi)

        delta_angle = (ray_angle - self.angle + math.pi) % (2 * math.pi) - math.pi

        self.angle += delta_angle

        x = self.x + math.cos(self.angle) * self.speed
        y = self.y + math.sin(self.angle) * self.speed

        if math.sqrt((x - p_x) ** 2 + (y - p_y) ** 2) <= 1:
            if self.frame_count > self.reload_time:
                player.health = max(player.health - self.damage, 0)
                self.frame_count = 0
        else:
            self.x = x
            self.y = y

        if self.frame_count <= self.reload_time:
            self.frame_count += self.frame

    def update(self):
        if self.health <= 0:
            self.is_alive = False
            return

        self.current_frame += self.delta_frame
        self.current_frame %= self.num_textures

    def draw(self, screen, depth, screen_x, player_x, player_y):
        proj_height = PROJ_COEFF / depth

        # view_angle = math.atan2(player_y - self.y, player_x - self.x)
        # relative_angle = (view_angle - self.angle) % (2 * math.pi)

        # angle_step = 2 * math.pi / self.num_textures
        # texture_index = int(relative_angle // angle_step) % self.num_textures

        scaled_texture = pygame.transform.scale(
            self.textures[int(self.current_frame)],
            (self.texture_width * (proj_height / self.texture_height), proj_height)
        )

        screen.blit(
            scaled_texture, (screen_x - scaled_texture.get_width() / 2, HEIGHT / 2 - proj_height / 2)
        )


class Barrel(Object):
    def __init__(self, x, y):
        texture_paths = ['data/textures/objects/barrel/barrel.png']
        super().__init__(x, y, texture_paths)


class Devil(Enemy):
    def __init__(self, x, y, damage, health, reload_time, angle=0, speed=PLAYER_SPEED):
        texture_paths = [f'data/textures/objects/devil/{i}.png' for i in range(
            8)]  # ['data/textures/objects/devil/devil.png']#[f'data/textures/objects/devil/{i}.png' for i in range(8)]
        super().__init__(x, y, texture_paths, damage, health, reload_time, angle, speed)


class Ghost(Enemy):
    def __init__(self, x, y, damage, health, reload_time, angle=0, speed=PLAYER_SPEED):
        texture_paths = ['data/textures/objects/ghost/ghost.png']
        super().__init__(x, y, texture_paths, damage, health, reload_time, angle, speed)


class Pin(Enemy):
    def __init__(self, x, y, damage, health, reload_time, angle=0, speed=PLAYER_SPEED):
        texture_paths = [f'data/textures/objects/pin/{i}.png' for i in range(8)]
        super().__init__(x, y, texture_paths, damage, health, reload_time, angle, speed)


objects = [
    Barrel(5, 5),
    Barrel(3, 4),
    Devil(21, 10, 20, 100, 2, speed=1.5),
    Barrel(22, 2),
    Devil(1.5, 9.5, 20, 100, 3, speed=1.5),
    Ghost(22, 4.5, 5, 20, 1, speed=PLAYER_RUNNING_SPEED),
    Pin(7, 7, 10, 50, 2, speed=2),
    Pin(7, 2, 10, 50, 2, speed=2)
]
