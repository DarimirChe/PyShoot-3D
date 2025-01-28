import pygame
from settings import *
import math


class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = PLAYER_SPEED / FPS
        self.angle_speed = PLAYER_ANGLE_SPEED / FPS
        self.sensitivity = MOUSE_SENSITIVITY

    def detect_collision_wall(self, x, y):
        self.dx = int(x)
        self.dy = int(y)
        next_rect = self.rect.copy()
        next_rect.move_ip(self.dx, self.dy)
        hit_indexes = next_rect.collidelistall(collision_walls)
        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = collision_walls[hit_index]
                if self.dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if self.dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top
            if abs(delta_x - delta_y) < 50:
                self.dx, self.dy = 0, 0
            elif delta_x > delta_y:
                self.dy = 0
            elif delta_y > delta_x:
                self.dx = 0

        self.x += self.dx
        self.y += self.dy

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)
            self.detect_collision_wall(self.dx, self.dy)
        if keys[pygame.K_s]:
            self.x -= self.speed * math.cos(self.angle)
            self.y -= self.speed * math.sin(self.angle)
            self.detect_collision_wall(self.dx, self.dy)
        if keys[pygame.K_d]:
            self.x -= self.speed * math.sin(self.angle)
            self.y += self.speed * math.cos(self.angle)
            self.detect_collision_wall(self.dx, self.dy)
        if keys[pygame.K_a]:
            self.x += self.speed * math.sin(self.angle)
            self.y -= self.speed * math.cos(self.angle)
            self.detect_collision_wall(self.dx, self.dy)

        if keys[pygame.K_LEFT]:
            self.angle -= self.angle_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.angle_speed

    def pos(self):
        return self.x, self.y, self.angle

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity
