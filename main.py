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
    pygame.mouse.set_visible(False)


    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.position)


    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
        player.movement()
        rendering.sky(player.angle)
        rendering.ground()
        rendering.raycasting(player, MAP)
        rendering.mini_map(player, MAP)
        rendering.fps(clock)
        pygame.display.flip()
        clock.tick()
