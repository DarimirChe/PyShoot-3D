import pygame
from widgets import Button
from settings import WIDTH


def pause_menu(screen, clock, FPS):
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    background = pygame.image.load('data/textures/background/pause_background.jpg')
    sprite.image = background
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    resume = Button(screen, 'Продолжить', y=300)
    go_to_main_menu = Button(screen, 'Выйти в главное меню', y=400)

    font = pygame.font.Font("data/fonts/PostalShrift.ttf", 100)
    text = font.render("Пауза", True, (255, 255, 255))
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if resume.on_button:
                    return "resume"
                if go_to_main_menu.on_button:
                    return "main_menu"

        all_sprites.draw(screen)
        resume.show_button()
        go_to_main_menu.show_button()
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 150))
        pygame.display.flip()
        clock.tick(FPS)
