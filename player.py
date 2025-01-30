import pygame
from settings import *
import math
from map import collision_walls


class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = PLAYER_SPEED / FPS
        self.angle_speed = PLAYER_ANGLE_SPEED / FPS
        self.sensitivity = MOUSE_SENSITIVITY
        self.side = 50
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
        self.collision_walls = collision_walls

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.collision_walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self):
        keys = pygame.key.get_pressed()
        self.rect.center = self.x, self.y
        if keys[pygame.K_w]:
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)
            dx = self.speed * math.cos(self.angle)
            dy = self.speed * math.sin(self.angle)
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            self.x -= self.speed * math.cos(self.angle)
            self.y -= self.speed * math.sin(self.angle)
            dx = -self.speed * math.cos(self.angle)
            dy = -self.speed * math.sin(self.angle)
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            self.x -= self.speed * math.sin(self.angle)
            self.y += self.speed * math.cos(self.angle)
            dx = -self.speed * math.cos(self.angle)
            dy = self.speed * math.sin(self.angle)
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            self.x += self.speed * math.sin(self.angle)
            self.y -= self.speed * math.cos(self.angle)
            dx = self.speed * math.cos(self.angle)
            dy = -self.speed * math.sin(self.angle)
            self.detect_collision(dx, dy)
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
