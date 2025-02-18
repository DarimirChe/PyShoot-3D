import pygame
from levels import levels
from widgets import Button
from settings import WIDTH, HEIGHT


def select_level(screen, clock, FPS):
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    background = pygame.image.load('data/textures/background/background.jpg')
    sprite.image = background
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    font = pygame.font.Font("data/fonts/PostalShrift.ttf", 60)

    exit_to_main_btn = Button(screen, 'главное меню', x=50, y=50, font_size=30)
    next_lvl = Button(screen, '>', x=1090, font_size=200)
    past_lvl = Button(screen, '<', x=50, font_size=200)
    play_lvl = Button(screen, 'ИГРАТЬ', y=560)

    selected_lvl = 0
    running = True

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if exit_to_main_btn.on_button:
                    return
                if next_lvl.on_button:
                    if selected_lvl == len(levels) - 1:
                        selected_lvl = 0
                    else:
                        selected_lvl += 1
                if past_lvl.on_button:
                    if selected_lvl == 0:
                        selected_lvl = len(levels) - 1
                    else:
                        selected_lvl -= 1
                if play_lvl.on_button:
                    return selected_lvl

        level_text = font.render(levels[selected_lvl]["name"], True, (138, 11, 11))

        all_sprites.draw(screen)
        screen.blit(level_text, (WIDTH / 2 - level_text.get_width() / 2, HEIGHT / 2 - level_text.get_height() / 2))
        exit_to_main_btn.show_button()
        next_lvl.show_button()
        past_lvl.show_button()
        play_lvl.show_button()
        pygame.display.flip()
        clock.tick(FPS)
