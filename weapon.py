class Weapon:
    def __init__(self, name, damage, fire_rate, bullet_type='bullet', do_explosion=False, explosion_range=0):
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate
        self.bullet_type = bullet_type
        self.do_explosion = do_explosion
        self.explosion_range = explosion_range
        if self.do_explosion and self.explosion_range == 0:
            self.explosion_range = 1

    def get_bullet_type(self):
        return self.bullet_type

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def get_fire_rate(self):
        return self.fire_rate

    def get_do_explosion(self):
        return self.do_explosion

    def get_explosion_range(self):
        return self.explosion_range

    def set_bullet_type(self, meaning):
        self.bullet_type = meaning

    def set_name(self, name):
        self.name = name

    def set_damage(self, meaning):
        self.damage = meaning

    def set_fire_rate(self, meaning):
        self.fire_rate = meaning

    def set_do_explosion(self, meaning):
        self.do_explosion = meaning

    def set_explosion_range(self, meaning):
        self.explosion_range = meaning

    def shoot(self):
        bt = self.get_bullet_type()
        if bt.lower() == 'bullet':
            b = Bullet(self.get_damage(), self.get_do_explosion(), self.get_explosion_range())
            return b
        elif bt.lower() == 'lazer':
            l = Lazer(self.get_damage(), self.get_do_explosion(), self.get_explosion_range())
            return l
        else:
            print('Error of bullet type: non-existent type')


#    def shoot_animation(self):


class Bullet:
    def __init__(self, damage, do_explosion, explosion_range):
        self.damage = damage
        self.do_explosion = do_explosion
        self.explosion_range = explosion_range


class Lazer:
    def __init__(self, damage, do_explosion, explosion_range):
        self.damage = damage
        self.do_explosion = do_explosion
        self.explosion_range = explosion_range
