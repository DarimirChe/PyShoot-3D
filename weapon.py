import pygame
import pathlib
from settings import *


ak_textures = 'ak47'


class Weapon:
    def __init__(self, name, fullness_clip, fire_rate, reload_time, damage, max_F_C, textures):
        self.name = name  # название
        self.damage = damage  # Уорн за попадание
        self.fire_rate = fire_rate  # время между выстрелами
        self.reload_time = reload_time  # reload time
        self.fullness_clip = fullness_clip  # количество патронов в магазине
        self.max_F_C = max_F_C  # максимальное количество патронов в магазине
        self.shooting = False
        self.reloading = False
        p = pathlib.Path(f'data/weapon/{textures}')
        for n in p.iterdir():
            if n == pathlib.Path(f'data/weapon/{textures}/reload'):
                self.reload_textures = [pygame.image.load(l) for l in n.iterdir()]

            elif n == pathlib.Path(f'data/weapon/{textures}/reload_and_aiming'):
                self.reload_aiming_textures = [pygame.image.load(l) for l in n.iterdir()]

            elif n == pathlib.Path(f'data/weapon/{textures}/shoot'):
                self.shoot_textures = [pygame.image.load(l) for l in n.iterdir()]

            elif n == pathlib.Path(f'data/weapon/{textures}/shoot_and_aiming'):
                self.shoot_aiming_textures = [pygame.image.load(l) for l in n.iterdir()]

            else:
                self.aiming_textures = [pygame.image.load(l) for l in n.iterdir()]

        self.current_frame = 0
        self.current_frame_image = self.shoot_textures[0]
        self.delta_frame_reload = len(self.reload_textures) / (self.reload_time * FPS)
        self.delta_frame_shoot = len(self.shoot_textures) / (self.fire_rate * FPS)

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def set_damage(self, num):
        self.damage = num

    def set_fire_rate(self, num):
        self.fire_rate = num

    def set_reload_time(self, num):
        self.reload_time = num

    def set_fullness_clip(self, num):
        self.fullness_clip = num

    def set_max_F_C(self, num):
        self.max_F_C = num

    def reload_weapon(self):
        self.set_fullness_clip(self.max_F_C)

    def get_frame(self):
        return self.current_frame_image

    def set_frame(self, shot_num=0, mod='s'):
        if mod == 'r':
            self.current_frame_image = self.reload_textures[shot_num]
        elif mod == 'ra':
            self.current_frame_image = self.reload_aiming_textures[shot_num]
        elif mod == 'sa':
            self.current_frame_image = self.shoot_aiming_textures[shot_num]
        elif mod == 'a':
            self.current_frame_image = self.aiming_textures[shot_num]
        elif mod == 's':
            self.current_frame_image = self.shoot_textures[shot_num]

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.current_frame = 0
            self.reload_weapon()
            self.reloading = True
        if self.reloading and self.shooting and pygame.mouse.get_pressed() == (1, 0, 0):  # попытка выстрела при выполнении перезарядки или выстрела
            pass  # можно сделать подачу сигнала игроку, что идёт перезарядка
        if not self.reloading and pygame.mouse.get_pressed() == (1, 0, 0):  # выполнение выстрела если не идёт перезарядка
            if self.shooting:
                pass
            else:
                self.current_frame = 0
                if self.fullness_clip > 1:
                    self.set_fullness_clip(self.fullness_clip - 1)
                    self.shooting = True
                elif self.fullness_clip == 1:
                    self.set_fullness_clip(self.fullness_clip - 1)
                    self.reloading = True

    def weapon_show(self, screen):
        s = int(self.current_frame // 1)
        if self.shooting:
            self.set_frame(s, 's')
            self.current_frame += self.delta_frame_shoot
        if self.reloading:
            self.set_frame(s, 'r')
            self.current_frame += self.delta_frame_reload
        else:
            self.set_frame()
        image = self.get_frame()
        w, h = image.get_width(), image.get_height()
        dest = (WIDTH - w, HEIGHT - h)
        if ((self.shooting and self.current_frame >= len(self.shoot_textures)) or
                (self.reloading and self.current_frame >= len(self.reload_textures))):
            if self.reloading:
                self.reloading = False
            elif self.shooting:
                self.shooting = False
            self.current_frame = 0
        screen.blit(image, dest)


class AK_47(Weapon):
    def __init__(self, name='AK-47', fullness_clip=30, fire_rate=0.25, reload_time=5, damage=23, max_F_C=30, texturs=ak_textures):
        super().__init__(name, fullness_clip, fire_rate, reload_time, damage, max_F_C, texturs)


#a = AK_47()