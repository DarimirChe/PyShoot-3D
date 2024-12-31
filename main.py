import pygame
from settings import *
from player import Player
from map import Map
from rendering import Rendering

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    MAP = Map()
    MAP.set_map("data/maps/map.txt")
    player = Player(2, 6, 0)
    rendering = Rendering(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        player.movement()
        rendering.sky(player.angle)
        rendering.ground()
        rendering.raycasting(player, MAP)
        rendering.mini_map(player, MAP)
        rendering.fps(clock)

        pygame.display.flip()
        clock.tick(FPS)