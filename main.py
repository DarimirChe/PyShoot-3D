from player import Player
from map import Map
from rendering import Rendering
from weapon import *
from main_menu import main_menu
from select_level import select_level
from pause_menu import pause_menu
from levels import levels

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

        MAP.set_map(f"data/maps/{level["map"]}")
        player = Player(*level["player_position"], MAP)

        rendering = Rendering(screen)
        play = True
        is_mouse = 1
        mouse_visible = False
        current_weapon = AK47()

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

            player.movement()
            current_weapon.update()
            if is_mouse == 1:
                player.mouse_control()
            rendering.sky(player.angle)
            rendering.ground()
            rendering.raycasting(player, MAP)
            rendering.objects(player, MAP)

            rendering.mini_map(player, MAP)
            rendering.fps(clock)

            current_weapon.handle_input()
            current_weapon.update()
            current_weapon.draw(screen)
            current_weapon.draw_ammo_info(screen)

            pygame.display.flip()
            clock.tick(FPS)
