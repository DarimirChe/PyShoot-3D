import pygame
from settings import *


class PyButton:
    def __init__(self, text, x, y, width, height, screen, primary_color=(175, 175, 175), secondary_color=(250, 250, 0), text_color=(255, 255, 255)):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.on_button = False
        self.primary_color, self.secondary_color = primary_color, secondary_color
        self.text_color = text_color

    def check_mouse_on(self):
        x, y, w, h = self.x, self.y, self.width, self.height
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x in range(x, x + w) and mouse_y in range(y, y + h):
            self.on_button = True
            return True
        else:
            self.on_button = False
            return False

    def show_button(self):
        self.check_mouse_on()
        x, y, w, h = self.x, self.y, self.width, self.height
        text_pos = (x + w // 4, y + h // 4)
        font = pygame.font.Font(None, self.height // 2)
        button_text = font.render(self.text, True, self.text_color)
        if self.on_button:
            self.screen.fill(self.secondary_color, pygame.Rect(x - 3, y - 3, w + 6, h + 6))
        self.screen.fill(self.primary_color, pygame.Rect(x, y, w, h))
        self.screen.blit(button_text, text_pos)


if __name__ == '__main__':
    pygame.init()
    size = width, height = WIDTH, HEIGHT
    pygame.display.set_caption('PyShoot 3D menu')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    running = True
    lvl_list = ['Level 1', 'Level 2', 'Level 3', 'Level 4']
    selected_lvl = 0

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    fon = pygame.image.load('data/textures/background/background.jpg')
    sprite.image = fon
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    font = pygame.font.Font(None, 60)
    button_text = font.render(lvl_list[selected_lvl], True, (255, 255, 255))

    play_button = PyButton('Play', 100, 400, 120, 60, screen)
    exit_game_button = PyButton('Exit', 100, 500, 120, 60, screen)
    exit_to_main_btn = PyButton('exit to main menu', 50, 50, 160, 36, screen)
    next_lvl = PyButton('>', 1090, 150, 140, 420, screen)
    past_lvl = PyButton('<', 50, 150, 140, 420, screen)
    play_lvl = PyButton('Play', 570, 560, 120, 60, screen)

    show_play = True
    show_levels = False
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP and show_play:
                if play_button.on_button:
                    show_play = False
                    show_levels = True
                if exit_game_button.on_button:
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP and show_levels:
                if exit_to_main_btn.on_button:
                    show_play = True
                    show_levels = False
                if next_lvl.on_button:
                    if selected_lvl == len(lvl_list) - 1:
                        selected_lvl = 0
                    else:
                        selected_lvl += 1
                if past_lvl.on_button:
                    if selected_lvl == 0:
                        selected_lvl = len(lvl_list) - 1
                    else:
                        selected_lvl -= 1
            button_text = font.render(lvl_list[selected_lvl], True, (255, 255, 255))
        all_sprites.draw(screen)
        if show_play:
            exit_game_button.show_button()
            play_button.show_button()
        if show_levels:
            screen.blit(button_text, (570, 300))
            exit_to_main_btn.show_button()
            next_lvl.show_button()
            past_lvl.show_button()
            play_lvl.show_button()
        pygame.display.flip()
        clock.tick(FPS)