import pygame
import time
from settings import *
from player import Player
from map import Map
from rendering import Rendering
from weapon import *
import math

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    MAP = Map()
    MAP.set_map("data/maps/map.txt")
    player = Player(2, 6, 0)
    rendering = Rendering(screen)
    reloading = False
    play = True
    is_mouse = 1
    mouse_visible = False
    shooting = False
    current_weapon = AK47()
    lastReloadTime = pygame.time.get_ticks()
    lastShootTime = pygame.time.get_ticks()
    while play:
        pygame.mouse.set_visible(mouse_visible)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    mouse_visible = not mouse_visible
                    is_mouse = - is_mouse
        player.movement()
        current_weapon.update()
        if is_mouse == 1:
            player.mouse_control()
        rendering.sky(player.angle)
        rendering.ground()
        rendering.raycasting(player, MAP)

        rendering.mini_map(player, MAP)
        rendering.fps(clock)

        current_weapon.handle_input()
        current_weapon.update()
        current_weapon.draw(screen)
        current_weapon.draw_ammo_info(screen)

        pygame.display.flip()
        clock.tick(FPS)
