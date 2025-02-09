import pygame
import time
from settings import *
from player import Player
from map import Map
from rendering import Rendering
from Weapon import Weapon
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
    current_weapon = Weapon('AK-47', 30, 0.5, 5, 23, 30)
    lastReloadTime = time.clock()
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
                if pygame.key.get_pressed()[pygame.K_r]:  # перезярдка по нажатию R
                    reloading = True
                    current_weapon.reload_weapon()
                    lastReloadTime = time.clock()
            if reloading and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (1, 0, 0):  # попытка выстрела при выполнении перезарядки
                pass  # можно сделать подачу сигнала игроку, что идёт перезарядка
            if not reloading and event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (1, 0, 0):  # выполнение выстрела если не идёт перезарядка
                if current_weapon.fullness_clip() < 1:
                    current_weapon.set_fullness_clip(current_weapon.fullness_clip() - 1)
                elif current_weapon.fullness_clip() == 1:
                    current_weapon.set_fullness_clip(current_weapon.fullness_clip() - 1)
                    reloading = True
                    current_weapon.reload_weapon()
            if lastReloadTime >= current_weapon.reload_time():  # окончание перезарядки по истечению таймера
                reloading = False
        player.movement()
        if is_mouse == 1:
            player.mouse_control()
        rendering.sky(player.angle)
        rendering.ground()
        rendering.raycasting(player, MAP)
        rendering.mini_map(player, MAP)
        rendering.fps(clock)
        pygame.display.flip()
        clock.tick(FPS)
