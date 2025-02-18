from player import Player
from map import Map
from rendering import Rendering
from weapon import *
from main_menu import main_menu
from select_level import select_level
from pause_menu import pause_menu
from win_window import win_window
from defeat_window import defeat_window
from levels import levels
import time

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('PyShoot 3D')
    clock = pygame.time.Clock()
    MAP = Map()
    is_open = True

    while is_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        level_index = None
        while level_index is None:
            main_menu(screen, clock, FPS)
            level_index = select_level(screen, clock, FPS)

        level = levels[level_index]

        objects = level["objects"]

        MAP.set_map(f"data/maps/{level["map"]}")
        player = Player(*level["player_position"], MAP)

        rendering = Rendering(screen, objects)
        play = True
        is_mouse = 1
        mouse_visible = False
        current_weapon = AK47(player, rendering, MAP, objects)

        start_time = time.time()
        while play:
            pygame.mouse.set_visible(mouse_visible)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        #mouse_visible = not mouse_visible
                        #is_mouse = - is_mouse
                        pygame.mouse.set_visible(True)

                        mode = pause_menu(screen, clock, FPS)
                        if mode == "resume":
                            pygame.mouse.set_visible(False)
                        elif mode == "main_menu":
                            play = False

            if is_mouse == 1:
                player.mouse_control()

            win = True
            for obj in objects:
                if hasattr(obj, "is_alive"):
                    if obj.is_alive:
                        obj.update()
                        obj.movement(player, MAP)
                        win = False
            if win:
                end_time = time.time()
                mode = win_window(screen, clock, FPS, end_time - start_time)
                mouse_visible = True
                pygame.mouse.set_visible(True)
                if mode == "main_menu":
                    play = False
            if player.health == 0:
                mode = defeat_window(screen, clock, FPS)
                if mode == "main_menu":
                    play = False

            player.movement()

            rendering.sky(player.angle)
            rendering.ground()
            rendering.raycasting(player, MAP)
            rendering.objects(player, MAP)

            rendering.mini_map(player, MAP)
            rendering.fps(clock)

            current_weapon.update()
            current_weapon.handle_input()
            current_weapon.update()
            current_weapon.draw(screen)
            current_weapon.draw_ammo_info(screen)

            rendering.health(player.health, player.max_health)

            pygame.display.flip()
            clock.tick(FPS)
