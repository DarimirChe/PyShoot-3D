import pygame


test_texturs = ['data/textures/weapon1beta1.jpg',
                'data/textures/weapon1beta2.jpg',
                'data/textures/weapon1beta3.jpg']


class Weapon:
    def __init__(self, name, fullness_clip, fire_rate, reload_time, damage, max_F_C, texturs):
        self.name = name  # название
        self.damage = damage  # Уорн за попадание
        self.fire_rate = fire_rate  # время между выстрелами
        self.reload_time = reload_time  # reload time
        self.fullness_clip = fullness_clip  # количество патронов в магазине
        self.max_F_C = max_F_C  # максимальное количество патронов в магазине
        self.texturs = texturs  # здесь будет список путей кнужным изображениям
        self.u_textur = texturs[0]

        self.can_shoot = True

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

    def set_shot(self, shot_num=1):  # в этот метод нужно вводить порядковый номер нужного кадра из списка, номера начинаются с 1
        self.u_textur = self.texturs[shot_num - 1]


class AK_47(Weapon):
    def __init__(self, name='AK-47', fullness_clip=30, fire_rate=0.25, reload_time=5, damage=23, max_F_C=30, texturs=test_texturs):
        super().__init__(name, fullness_clip, fire_rate, reload_time, damage, max_F_C, texturs)


class Bullet:
    def __init__(self, damage, s_pos: tuple, vector: tuple):
        self.damage = damage
        self.x1 = s_pos[0]
        self.y1 = s_pos[1]
        self.vector = vector

    def x1(self):
        return self.x1

    def y1(self):
        return self.y1

    def vector(self):
        return self.vector


