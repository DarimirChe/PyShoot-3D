import pygame


ak_texturs = ['data/ak47/shoot/0.png',
              'data/ak47/shoot/1.png',
              'data/ak47/reload/0.png',
              'data/ak47/reload/1.png',
              'data/ak47/reload/2.png',
              'data/ak47/reload/3.png',
              'data/ak47/reload/4.png',
              'data/ak47/reload/5.png',
              'data/ak47/reload/6.png',
              'data/ak47/reload/7.png',
              'data/ak47/reload/8.png',
              'data/ak47/reload/9.png',
              'data/ak47/reload/10.png',
              'data/ak47/reload/11.png',
              'data/ak47/reload/12.png',
              'data/ak47/reload/13.png',
              'data/ak47/reload/14.png',
              'data/ak47/reload/15.png',
              'data/ak47/reload/16.png',
              'data/ak47/reload/17.png',
              'data/ak47/reload/18.png',
              'data/ak47/reload_and_aiming/0.png',
              'data/ak47/reload_and_aiming/1.png',
              'data/ak47/reload_and_aiming/2.png',
              'data/ak47/reload_and_aiming/3.png',
              'data/ak47/shoot_and_aiming/0.png',
              'data/ak47/shoot_and_aiming/1.png',
              'data/ak47/shoot_and_aiming/2.png',]
#              'data/ak47/aiming/0.png',
#              'data/ak47/aiming/1.png',
#              'data/ak47/aiming/2.png'
#              ]


class Weapon:
    def __init__(self, name, fullness_clip, fire_rate, reload_time, damage, max_F_C, texturs):
        self.name = name  # название
        self.damage = damage  # Уорн за попадание
        self.fire_rate = fire_rate  # время между выстрелами
        self.reload_time = reload_time  # reload time
        self.fullness_clip = fullness_clip  # количество патронов в магазине
        self.max_F_C = max_F_C  # максимальное количество патронов в магазине
        self.texturs = texturs  # здесь будет список путей кнужным изображениям
        self.s_t = []
        self.r_t = []
        self.r_a_t = []
        self.s_a_t = []
#        self.a_t = []

        for textur in texturs:
            t = textur.split('/')
            im = pygame.image.load(textur)
            if 'shoot' in t:
                self.s_t.append(im)
            elif 'reload' in t:
                self.r_t.append(im)
            elif 'reload_and_aiming' in t:
                self.r_a_t.append(im)
            elif 'shoot_and_aiming' in t:
                self.s_a_t.append(im)
#            elif 'aiming' in t:
#                self.a_t.append(im)
        self.u_textur = self.s_t[0]
        self.time_per_frame_r = self.reload_time * 200 / (len(self.r_t) - 1)
        self.time_per_frame_s = self.fire_rate * 200 / (len(self.s_t) - 1)
#        self.can_shoot = True

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
    def __init__(self, name='AK-47', fullness_clip=30, fire_rate=0.25, reload_time=5, damage=23, max_F_C=30, texturs=ak_texturs):
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


