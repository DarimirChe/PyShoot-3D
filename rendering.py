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

    def objects(self, player, MAP):
        x, y, player_angle = player.pos()
        for object in objects:
            ray_angle = math.atan(abs(object[1] - y) / abs(object[0] - x)) #- player_angle
            if ray_angle:
                pass
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
                            break
            # Ищем ближайщую стену пересечения основываясь на координатах h_Px, h_Py, v_Px, v_Py
            depth_h = abs(x - h_Px) ** 2 + abs(y - h_Py) ** 2
            depth_v = abs(x - v_Px) ** 2 + abs(y - v_Py) ** 2
            depth = min(depth_v, depth_h)

            object_depth = abs(object[1] - y) ** 2 + abs(object[0] - x) ** 2

            if object_depth < depth:
                '''
                proj_height = PROJ_COEFF / depth
                wall_column = texture.subsurface(int(texture.get_width() * offset), 0, 1, texture.get_height())
                wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
                self.screen.blit(wall_column, (ray * SCALE, HEIGHT / 2 - proj_height / 2))
                '''
                proj_height = PROJ_COEFF / math.sqrt(depth)
                t = pygame.image.load('data/textures/objects/barrel.jpg').convert()
                self.screen.blit(t, (ray_angle * SCALE, HEIGHT / 2 - proj_height / 2))

    def objects2(self, player, MAP):
        x, y, player_angle = player.pos()
        for object in objects:
            obj_x, obj_y = object[0], object[1]
            dx = obj_x - x
            dy = obj_y - y
            distance_to_object = math.sqrt(dx ** 2 + dy ** 2)

            # Вычисляем угол к объекту
            ray_angle = math.atan2(dy, dx) - player_angle
            ray_angle = (ray_angle + math.pi) % (2 * math.pi) - math.pi  # Нормализация угла

            # Проверяем, находится ли объект в поле зрения
            if abs(ray_angle) < FOV / 2:
                # Проверка на столкновение со стенами
                depth_h, depth_v = float('inf'), float('inf')

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
                                break
                # Ищем ближайщую стену пересечения основываясь на координатах h_Px, h_Py, v_Px, v_Py
                depth_h = abs(x - h_Px) ** 2 + abs(y - h_Py) ** 2
                depth_v = abs(x - v_Px) ** 2 + abs(y - v_Py) ** 2
                depth = min(depth_v, depth_h)

                # Если объект ближе, чем стена, рисуем его
                if distance_to_object < depth:
                    proj_height = PROJ_COEFF / distance_to_object

                    # Вычисляем положение по горизонтали
                    screen_x = (ray_angle + (FOV / 2)) * (WIDTH / FOV)
                    #screen_x = int(max(0, min(WIDTH - 1, screen_x)))

                    # Загружаем текстуру объекта
                    t = pygame.image.load('data/textures/objects/barrel.png').convert()
                    texture_width = t.get_width()
                    texture_height = t.get_height()

                    # Вычисляем смещение для центрирования объекта
                    offset = (screen_x % 1) * texture_width

                    # Масштабируем текстуру до нужной высоты
                    scaled_texture = pygame.transform.scale(t, (
                    int(texture_width * (proj_height / texture_height)), int(proj_height)))

                    # Отображаем объект на экране
                    self.screen.blit(scaled_texture,
                                     (screen_x - scaled_texture.get_width() // 2, HEIGHT / 2 - proj_height // 2))




