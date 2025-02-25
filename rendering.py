import math

import pygame
from settings import *


class Rendering:
    def __init__(self, screen):
        self.screen = screen
        self.textures = {"1": pygame.image.load('data/textures/1.jpg').convert(),
                         "2": pygame.image.load('data/textures/2.jpg').convert(),
                         "Sky": pygame.image.load('data/textures/sky.jpg').convert()
                         }

    def raycasting(self, player, MAP):
        x, y, angle = player.pos()
        MAP = MAP.MAP

        px = x % 1
        py = y % 1
        ray_angle = angle - FOV / 2
        delta_angle = FOV / NUM_RAYS
        for ray in range(NUM_RAYS):
            # Горизонтальные стены
            if math.tan(ray_angle) != 0:
                if math.sin(ray_angle) > 0:
                    xi = (1 - py) / math.tan(ray_angle)
                    dx = 1 / math.tan(ray_angle)
                    for i in range(len(MAP)):
                        h_Px = x + xi + dx * i
                        h_Py = y // 1 + 1 + i
                        row, col = int(h_Py), int(h_Px // 1)
                        if 0 <= col < len(MAP[0]) and 0 <= row < len(MAP):
                            if MAP[row][col] != "0":
                                texture_h = self.textures[MAP[row][col]]
                                break
                else:
                    xi = -py / math.tan(ray_angle)
                    dx = 1 / math.tan(ray_angle)
                    for i in range(len(MAP)):
                        h_Px = x + xi - dx * i
                        h_Py = y // 1 - i
                        row, col = int(h_Py) - 1, int(h_Px // 1)
                        if 0 <= col < len(MAP[0]) and 0 <= row < len(MAP):
                            if MAP[row][col] != "0":
                                texture_h = self.textures[MAP[row][col]]
                                break
            # Вертикальные стены
            if math.cos(ray_angle) > 0:
                yi = (1 - px) * math.tan(ray_angle)
                dy = math.tan(ray_angle)
                for i in range(len(MAP[0])):
                    v_Px = x // 1 + 1 + i
                    v_Py = y + yi + dy * i
                    row, col = int(v_Py // 1), int(v_Px)
                    if 0 <= col < len(MAP[0]) and 0 <= row < len(MAP):
                        if MAP[row][col] != "0":
                            texture_v = self.textures[MAP[row][col]]
                            break
            else:
                yi = px * math.tan(ray_angle)
                dy = math.tan(ray_angle)
                for i in range(len(MAP[0])):
                    v_Px = x // 1 - i
                    v_Py = y - yi - dy * i
                    row, col = int(v_Py // 1), int(v_Px) - 1
                    if 0 <= col < len(MAP[0]) and 0 <= row < len(MAP):
                        if MAP[row][col] != "0":
                            texture_v = self.textures[MAP[row][col]]
                            break

            # Ищем ближайщую стену пересечения основываясь на координатах h_Px, h_Py, v_Px, v_Py
            depth_h = abs(x - h_Px) ** 2 + abs(y - h_Py) ** 2
            depth_v = abs(x - v_Px) ** 2 + abs(y - v_Py) ** 2

            depth, offset, texture = (depth_v, v_Py, texture_v) if depth_v < depth_h else (depth_h, h_Px, texture_h)
            depth = math.sqrt(depth)
            offset %= 1

            depth *= math.cos(angle - ray_angle)
            proj_height = PROJ_COEFF / depth

            wall_column = texture.subsurface(int(texture.get_width() * offset), 0, 1, texture.get_height())
            wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
            self.screen.blit(wall_column, (ray * SCALE, HEIGHT / 2 - proj_height / 2))

            ray_angle += delta_angle

    def sky(self, angle):
        w = self.textures["Sky"].get_width()
        sky_offset = -w * (math.degrees(angle) % 360 / 360)
        self.screen.blit(self.textures["Sky"], (sky_offset, 0))
        self.screen.blit(self.textures["Sky"], (sky_offset + w, 0))

    def ground(self):
        pygame.draw.rect(self.screen, (80, 111, 80), (0, HEIGHT / 2, WIDTH, HEIGHT / 2))

    def fps(self, clock):
        font = pygame.font.Font(None, 50)
        fps = font.render(str(int(clock.get_fps())), True, (255, 250, 0))
        self.screen.blit(fps, (0, 0))

    def mini_map(self, player, MAP):
        x, y, angle = player.pos()
        MAP = MAP.MAP
        tile = 15
        for row in range(len(MAP)):
            for column in range(len(MAP[row])):
                pygame.draw.rect(self.screen, "white", (tile * column, tile * row, tile, tile), MAP[row][column] == "0")
        pygame.draw.circle(self.screen, "green", (x * tile, y * tile), 5)
        pygame.draw.line(self.screen, "red", (x * tile, y * tile),
                         ((x + 0.5 * math.cos(angle)) * tile, (y + 0.5 * math.sin(angle)) * tile))
