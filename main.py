from player import Player
from map import Map
from rendering import Rendering
from weapon import *
from objects import objects

if __name__ == '__main__':
    pygame.init()
    speed = PLAYER_SPEED
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    MAP = Map()
    MAP.set_map("data/maps/map.txt")
    player = Player(2, 6, 0, MAP)
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
                    mouse_visible = not mouse_visible
                    is_mouse = - is_mouse

        if is_mouse == 1:
            player.mouse_control()

        for obj in objects:
            if hasattr(obj, 'movement'):
                obj.movement(player)

        player.movement()

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

        rendering.health(player.health, player.max_health)

        pygame.display.flip()
        clock.tick(FPS)
