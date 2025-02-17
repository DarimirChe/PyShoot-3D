import pygame
from settings import *
import math
from map import Map


class Player:
    def __init__(self, x, y, angle, MAP):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = PLAYER_SPEED / FPS
        self.angle_speed = PLAYER_ANGLE_SPEED / FPS
        self.sensitivity = MOUSE_SENSITIVITY
        self.MAP = MAP.MAP
        self.map_edge_y = len(self.MAP)
        self.map_edge_x = len(self.MAP[0])

    def detect_collision(self, dx, dy):
        radius = 0.1 if dx > 0 else -0.1
        if self.MAP[int(self.y)][int(self.x + dx + radius)] == "0":
            self.x += dx
        radius = 0.1 if dy > 0 else -0.1
        if self.MAP[int(self.y + dy + radius)][int(self.x)] == "0":
            self.y += dy

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx = self.speed * math.cos(self.angle)
            dy = self.speed * math.sin(self.angle)
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -self.speed * math.cos(self.angle)
            dy = -self.speed * math.sin(self.angle)
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -self.speed * math.sin(self.angle)
            dy = self.speed * math.cos(self.angle)
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = self.speed * math.sin(self.angle)
            dy = -self.speed * math.cos(self.angle)
            self.detect_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= self.angle_speed
            self.angle %= -2 * math.pi
        if keys[pygame.K_RIGHT]:
            self.angle += self.angle_speed
            self.angle %= -2 * math.pi

    def pos(self):
        return self.x, self.y, self.angle

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity
        self.angle %= -2 * math.pi
