import pygame
import pathlib


ak_textures = 'ak47'


class Weapon:
    def __init__(self, name, fullness_clip, fire_rate, reload_time, damage, max_F_C, textures):
        self.name = name  # название
        self.damage = damage  # Уорн за попадание
        self.fire_rate = fire_rate  # время между выстрелами
        self.reload_time = reload_time  # reload time
        self.fullness_clip = fullness_clip  # количество патронов в магазине
        self.max_F_C = max_F_C  # максимальное количество патронов в магазине
        self.s_t = []
        self.r_t = []
        self.r_a_t = []
        self.s_a_t = []
        self.a_t = []
        p = pathlib.Path(f'data/weapon/{textures}')
        self.texturs = []
        for n in p.iterdir():
            if n == pathlib.Path(f'data/weapon/{textures}/reload'):
                self.r_t = [pygame.image.load(l) for l in n.iterdir()]

            elif n == pathlib.Path(f'data/weapon/{textures}/reload_and_aiming'):
                self.r_a_t = [pygame.image.load(l) for l in n.iterdir()]

            elif n == pathlib.Path(f'data/weapon/{textures}/shoot'):
                self.s_t = [pygame.image.load(l) for l in n.iterdir()]

            elif n == pathlib.Path(f'data/weapon/{textures}/shoot_and_aiming'):
                self.s_a_t = [pygame.image.load(l) for l in n.iterdir()]

            else:
                self.a_t = [pygame.image.load(l) for l in n.iterdir()]

        self.u_textur = self.s_t[0]
        self.time_per_frame_r = self.reload_time * 200 / (len(self.r_t) - 1)
        self.time_per_frame_s = self.fire_rate * 200 / (len(self.s_t) - 1)

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

    def get_shot(self):
        return self.u_textur

    def set_shot(self, shot_num=0, mod='s'):  # в этот метод нужно вводить порядковый номер нужного кадра из списка, номера начинаются с 1
        if mod == 'r':
            self.u_textur = self.r_t[shot_num]
        elif mod == 'ra':
            self.u_textur = self.r_a_t[shot_num]
        elif mod == 'sa':
            self.u_textur = self.s_a_t[shot_num]
#        elif mod == 'a':
#            self.u_textur = self.a_t[shot_num]
        elif mod == 's':
            self.u_textur = self.s_t[shot_num]


class AK_47(Weapon):
    def __init__(self, name='AK-47', fullness_clip=30, fire_rate=0.25, reload_time=5, damage=23, max_F_C=30, texturs=ak_textures):
        super().__init__(name, fullness_clip, fire_rate, reload_time, damage, max_F_C, texturs)


a = AK_47()