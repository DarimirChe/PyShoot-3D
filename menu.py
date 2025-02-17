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

    def get_pressed(self):
        get_pressed = any(pygame.mouse.get_pressed())
        if get_pressed and self.on_button:
            return True
        else:
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
#    fon = pygame.image.load('')
    play_button = PyButton('Play', 100, 100, 120, 60, screen)
    lvl1 = PyButton('Level 1', 100, 100, 120, 60, screen)
    lvl2 = PyButton('Level 2', 100, 200, 120, 60, screen)
    show_play = True
    show_levels = False
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if show_play:
            play_button.show_button()
            if play_button.get_pressed():
                show_play = not show_play
                show_levels = not show_levels
        if show_levels:
            lvl1.show_button()
            lvl2.show_button()
            if lvl1.get_pressed() or lvl2.get_pressed():
                show_play = not show_play
                show_levels = not show_levels
        pygame.display.flip()
        clock.tick(FPS)