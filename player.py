import pygame
from settings import *
import math
from map import MAP


class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = PLAYER_SPEED / FPS
        self.angle_speed = PLAYER_ANGLE_SPEED / FPS
        self.sensitivity = MOUSE_SENSITIVITY
        self.MAP = MAP

    def detect_collision(self, dx, dy):
        if self.MAP[int(self.y + dy)][int(self.x + dx)] == "0":
            self.x += dx
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
            dx = -self.speed * math.cos(self.angle)
            dy = self.speed * math.sin(self.angle)
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
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
