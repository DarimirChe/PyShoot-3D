import pygame
from widgets import Button
from settings import WIDTH


def win_window(screen, clock, FPS, time):
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    background = pygame.image.load('data/textures/background/win.jpg')
    sprite.image = background
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    #next_level = Button(screen, 'Следующий уровень', y=400)
    to_main_menu = Button(screen, 'В главное меню', y=500)

    font = pygame.font.Font("data/fonts/PostalShrift.ttf", 100)
    text = font.render("Победа!", True, (12, 84, 16))
    font = pygame.font.Font("data/fonts/PostalShrift.ttf", 50)
    text_time = font.render(f"Ваш результат: {round(time)} сек", True, (12, 84, 16))
    pygame.mouse.set_visible(True)
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                #if next_level.on_button:
                #    return "next_level"
                if to_main_menu.on_button:
                    return "main_menu"
        all_sprites.draw(screen)
        #next_level.show_button()
        to_main_menu.show_button()
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 100))
        screen.blit(text_time, (WIDTH / 2 - text_time.get_width() / 2, 200))
        pygame.display.flip()
        clock.tick(FPS)
