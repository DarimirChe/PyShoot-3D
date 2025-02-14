import pygame
from settings import *
from player import Player
from map import Map
from rendering import Rendering
import math

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    MAP = Map()
    MAP.set_map("data/maps/map.txt")
    player = Player(2, 6, 0)
    rendering = Rendering(screen)
    play = True
    is_mouse = 1
    mouse_visible = False
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
        if is_mouse == 1:
            player.mouse_control()
        rendering.sky(player.angle)
        rendering.ground()
        rendering.raycasting(player, MAP)
        rendering.objects(player, MAP)
        rendering.mini_map(player, MAP)
        rendering.fps(clock)
        pygame.display.flip()
        clock.tick(FPS)
