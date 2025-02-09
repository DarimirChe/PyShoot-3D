class Weapon:
    def __init__(self, name, fullness_clip, fire_rate, reload_time, damage, max_F_C):
        self.name = name  # название
        self.damage = damage  # Уорн за попадание
        self.fire_rate = fire_rate  # время между выстрелами
        self.reload_time = reload_time  # reload time
        self.fullness_clip = fullness_clip  # количество патронов в магазине
        self.max_F_C = max_F_C  # максимальное количество патронов в магазине
        self.can_shoot = True

    def get_name(self):
        return self.name

    def damage(self):
        return self.damage

    def fire_rate(self):
        return self.fire_rate

    def reload_time(self):
        return self.reload_time

    def fullness_clip(self):
        return self.fullness_clip

    def max_F_C(self):
        return self.max_F_C

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
        self.set_fullness_clip(self.max_F_C())
#    def shoot_animation(self):


class Bullet:
    def __init__(self, damage, pos, vector):
        self.damage = damage
        self.x = pos[0]
        self.y = pos[1]
        self.vector = vector

    def x(self):
        return self.x

    def y(self):
        return self.y

    def set_x(self, num):
        self.x = num

    def set_y(self, num):
        self.y = num



