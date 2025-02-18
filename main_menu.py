import pygame
from widgets import Button
from settings import WIDTH


def main_menu(screen, clock, FPS):
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    background = pygame.image.load('data/textures/background/background.jpg')
    sprite.image = background
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    play_button = Button(screen, 'Играть', y=400)
    exit_game_button = Button(screen, 'Выход', y=500)

    font = pygame.font.Font("data/fonts/Doom2016Text.ttf", 200)
    text = font.render("PyShoot 3D", True, (255, 255, 255))

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.on_button:
                    return
                if exit_game_button.on_button:
                    pygame.quit()
                    exit()
        all_sprites.draw(screen)
        exit_game_button.show_button()
        play_button.show_button()
        screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 100))
        pygame.display.flip()
        clock.tick(FPS)
