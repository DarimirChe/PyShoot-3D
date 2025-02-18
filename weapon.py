import pygame
from pathlib import Path
from settings import *
from objects import objects


class Weapon:
    def __init__(self, name, mag_size, fire_rate, reload_time, damage, textures_folder, player, rendering, MAP):
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.reload_time = reload_time
        self.mag_size = mag_size
        self.ammo = mag_size
        self.is_shooting = False
        self.is_reloading = False
        self.is_aiming = False
        self.current_frame = 0
        self.last_shot_time = 0

        self.load_textures(textures_folder)

        # Скорость смены кадров
        self.delta_frame_reload = len(self.reload_textures) / (self.reload_time * FPS)
        self.delta_frame_shoot = len(self.shoot_textures) / (self.fire_rate * FPS)

        self.current_texture = self.shoot_textures[0]

        self.player = player
        self.rendering = rendering
        self.MAP = MAP

    def load_textures(self, folder):
        path = Path(f'data/weapon/{folder}')
        self.reload_textures = []
        self.reload_aiming_textures = []
        self.shoot_textures = []
        self.shoot_aiming_textures = []
        self.aiming_textures = []

        for subfolder in path.iterdir():
            textures = [pygame.image.load(str(img)) for img in sorted(subfolder.iterdir())]
            match subfolder.name:
                case 'reload':
                    self.reload_textures = textures
                case 'reload_and_aiming':
                    self.reload_aiming_textures = textures
                case 'shoot':
                    self.shoot_textures = textures
                case 'shoot_and_aiming':
                    self.shoot_aiming_textures = textures
                case _:
                    self.aiming_textures = textures

    def handle_input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if mouse[0]:
            self.fire()

        self.is_aiming = bool(mouse[2])

        if keys[pygame.K_r]:
            self.reload_weapon()

    def fire(self):
        if self.is_shooting or self.is_reloading or self.ammo == 0:
            return

        # Ограничение по скорострельности
        if pygame.time.get_ticks() - self.last_shot_time < self.fire_rate * 1000:
            return

        pygame.mixer.music.load("data/sounds/ak47-shoot.mp3")
        pygame.mixer.music.play()
        self.is_shooting = True
        self.current_frame = 0
        self.ammo -= 1
        self.last_shot_time = pygame.time.get_ticks()

        if self.ammo == 0:
            self.reload_weapon()

        x, y, angle = self.player.pos()

        sorted_objects = []
        for obj in objects:
            if hasattr(obj, "is_alive"):
                if not obj.is_alive:
                    continue
            else:
                continue
            obj_x, obj_y = obj.pos()
            sorted_objects.append([obj, (obj_y - y) ** 2 + (obj_x - x) ** 2])
        sorted_objects.sort(key=lambda x: x[1])

        for obj in sorted_objects:
            obj_x, obj_y = obj[0].pos()
            # Вычисляем угол к объекту
            ray_angle = math.atan2(obj_y - y, obj_x - x)
            ray_angle = (ray_angle + 2 * math.pi) % (2 * math.pi)
            delta_angle = (ray_angle - angle + math.pi) % (2 * math.pi) - math.pi
            alfa = math.atan2(obj[0].size / 2, obj[1])
            thetta = angle + delta_angle
            if thetta - alfa <= angle <= thetta + alfa:
                if math.sqrt(obj[1]) <= self.rendering.ray_cast(self.player, self.MAP, angle)[0]:
                    obj[0].health -= self.damage
                    return

    def reload_weapon(self):
        if not self.is_reloading:
            pygame.mixer.music.load("data/sounds/ak47_reload.mp3")
            pygame.mixer.music.play()
            self.is_reloading = True
            self.current_frame = 0

    def update(self):
        if self.is_reloading:
            textures = self.reload_aiming_textures if self.is_aiming else self.reload_textures
            total_frames = len(textures)
            self.current_frame += (1 / (self.reload_time * FPS)) * total_frames  # Процент выполнения анимации
            frame_index = min(int(self.current_frame), total_frames - 1)
            self.current_texture = textures[frame_index]

            if self.current_frame >= total_frames:  # Завершение анимации
                self.is_reloading = False
                self.ammo = self.mag_size
                self.current_frame = 0

        elif self.is_shooting:
            textures = self.shoot_aiming_textures if self.is_aiming else self.shoot_textures
            total_frames = len(textures)
            self.current_frame += (1 / (self.fire_rate * FPS)) * total_frames
            frame_index = min(int(self.current_frame), total_frames - 1)
            self.current_texture = textures[frame_index]

            if self.current_frame >= total_frames:
                self.is_shooting = False
                self.current_frame = 0
        elif self.is_aiming and self.aiming_textures:
            textures = self.aiming_textures
            total_frames = len(textures)
            self.current_frame += (1 / (0.2 * FPS)) * total_frames
            frame_index = min(int(self.current_frame), total_frames - 1)
            self.current_texture = textures[frame_index]
        else:
            self.current_texture = self.shoot_textures[0]
            self.current_frame = 0

    def draw(self, screen):
        w, h = self.current_texture.get_width(), self.current_texture.get_height()
        pos = (WIDTH - w, HEIGHT - h)
        screen.blit(self.current_texture, pos)

    def draw_ammo_info(self, screen):
        font_size = 50
        font = pygame.font.Font(None, font_size)

        padding = 5

        ammo_text_y = HEIGHT - padding - font_size
        weapon_name_y = ammo_text_y - padding - font_size

        weapon_name_surface = font.render(self.name, True, (255, 250, 0))
        screen.blit(weapon_name_surface, (WIDTH - weapon_name_surface.get_width() - padding, weapon_name_y))

        if self.is_reloading:
            ammo_text = "Перезарядка"
        else:
            ammo_text = f"Патронов: {self.ammo}/{self.mag_size}"

        # Цвет текста в зависимости от количества патронов
        if self.mag_size > 0:
            ammo_ratio = self.ammo / self.mag_size
            red_value = int(255 * (1 - ammo_ratio))  # Красный увеличивается при уменьшении патронов
            green_value = int(255 * ammo_ratio)  # Зеленый уменьшается при уменьшении патронов
        else:
            red_value = 255
            green_value = 0

        ammo_color = (red_value, green_value, 0)

        ammo_text_surface = font.render(ammo_text, True, ammo_color)
        screen.blit(ammo_text_surface, (WIDTH - ammo_text_surface.get_width() - padding, ammo_text_y))


class AK47(Weapon):
    def __init__(self, player, rendering, MAP):
        super().__init__(
            name="AK-47",
            mag_size=30,
            fire_rate=0.2,
            reload_time=2,
            damage=23,
            textures_folder="ak47",
            player=player,
            rendering=rendering,
            MAP=MAP
        )
