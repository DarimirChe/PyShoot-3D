import pygame
from settings import WIDTH, HEIGHT


class Button:
    def __init__(self, screen, text, x=-1, y=-1, font_size=50, primary_color=(175, 175, 175),
                 secondary_color=(138, 11, 11), text_color=(138, 11, 11), padding=20):
        self.text = text
        self.screen = screen
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.text_color = text_color
        self.font_size = font_size
        self.font = pygame.font.Font("data/fonts/PostalShrift.ttf", font_size)
        self.button_text = self.font.render(self.text, True, self.text_color)
        self.width, self.height = self.button_text.get_width() + padding, self.button_text.get_height() + padding

        self.x = x
        self.y = y
        if x == -1:
            self.x = WIDTH / 2 - self.width / 2
        if y == -1:
            self.y = HEIGHT / 2 - self.height / 2

        self.on_button = False

    def check_mouse_on(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.on_button = (self.x <= mouse_x <= self.x + self.width) and (self.y <= mouse_y <= self.y + self.height)
        return self.on_button

    def show_button(self):
        self.check_mouse_on()

        if self.on_button:
            self.screen.fill(self.secondary_color, (self.x - 3, self.y - 3, self.width + 6, self.height + 6))

        self.screen.fill(self.primary_color, (self.x, self.y, self.width, self.height))

        text_pos = (self.x + (self.width - self.button_text.get_width()) // 2,
                    self.y + (self.height - self.button_text.get_height()) // 2)
        self.screen.blit(self.button_text, text_pos)
