import pygame
from settings import *
import math
from map import Map


class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = PLAYER_SPEED / FPS
        self.running_speed = PLAYER_RUNNING_SPEED
        self.angle_speed = PLAYER_ANGLE_SPEED / FPS
        self.sensitivity = MOUSE_SENSITIVITY

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
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.speed += 0.01
            if self.speed >= self.running_speed:
                self.speed = self.running_speed
        else:
            self.speed = PLAYER_SPEED / FPS

    def pos(self):
        return self.x, self.y, self.angle

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity
