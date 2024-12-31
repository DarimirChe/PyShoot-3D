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

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)
        if keys[pygame.K_s]:
            self.x -= self.speed * math.cos(self.angle)
            self.y -= self.speed * math.sin(self.angle)
        if keys[pygame.K_d]:
            self.x -= self.speed * math.sin(self.angle)
            self.y += self.speed * math.cos(self.angle)
        if keys[pygame.K_a]:
            self.x += self.speed * math.sin(self.angle)
            self.y -= self.speed * math.cos(self.angle)
        if keys[pygame.K_LEFT]:
            self.angle -= self.angle_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.angle_speed

    def pos(self):
        return self.x, self.y, self.angle
