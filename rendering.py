import math

import pygame
from settings import *
from objects import objects


class Rendering:
    def __init__(self, screen):
        self.screen = screen
        self.textures = {"1": pygame.image.load('data/textures/walls/1.jpg').convert(),
                         "2": pygame.image.load('data/textures/walls/2.jpg').convert(),
                         "Sky": pygame.image.load('data/textures/sky/sky.jpg').convert()
                         }

    def raycasting(self, player, MAP):
        x, y, angle = player.pos()

        ray_angle = angle - FOV / 2
        delta_angle = FOV / NUM_RAYS
        for ray in range(NUM_RAYS):
            depth, offset, texture = self.ray_cast(player, MAP, ray_angle)
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

    def objects(self, player, MAP):
        x, y, angle = player.pos()

        for obj in objects:
            obj_x, obj_y = obj[0], obj[1]

            # Вычисляем угол к объекту
            ray_angle = math.atan2(obj_y - y, obj_x - x)
            ray_angle = (ray_angle + 2 * math.pi) % (2 * math.pi)

            delta_angle = (ray_angle - angle + math.pi) % (2 * math.pi) - math.pi

            # Проверяем, находится ли объект в поле зрения
            if abs(delta_angle) < FOV / 2:
                depth = self.ray_cast(player, MAP, ray_angle)[0]
                # Вычисляем расстояние до объекта
                object_depth = math.sqrt((obj[1] - y) ** 2 + (obj[0] - x) ** 2)

                if object_depth <= depth:
                    proj_height = PROJ_COEFF / object_depth

                    # Вычисляем положение объекта на экране
                    screen_x = (delta_angle + (FOV / 2)) * (WIDTH / FOV)

                    t = pygame.image.load('data/textures/objects/barrel.png')
                    texture_width = t.get_width()
                    texture_height = t.get_height()

                    scaled_texture = pygame.transform.scale(
                        t, (texture_width * (proj_height / texture_height), proj_height)
                    )

                    self.screen.blit(
                        scaled_texture, (screen_x - scaled_texture.get_width() / 2, HEIGHT / 2 - proj_height / 2)
                    )

    def ray_cast(self, player, MAP, ray_angle):
        x, y, angle = player.pos()
        MAP = MAP.MAP

        px = x % 1
        py = y % 1
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
        return depth, offset, texture
