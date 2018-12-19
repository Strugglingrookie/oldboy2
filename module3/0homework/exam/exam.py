class People:
    def __init__(self, name, life, weapon, sex, blood):
        self.name = name
        self.life = life
        self.weapon = weapon
        self.sex = sex
        self.blood = blood

    def attack(self, other):
        other.life -= self.blood
        print("%s 攻击了 %s ，失去 %s 生命值" % (self.name, other.name, self.blood))


class Police(People):
    def attack(self, other):
        if isinstance(other, Police):
            print("Can't attack your similar!")
        else:
            super().attack(other)


class Terrorist(People):
    def attack(self, other):
        if isinstance(other, Terrorist):
            print("Can't attack your similar!")
        else:
            super().attack(other)


P = Police("xg", 100, "AK47", "男", 10)
P2 = Police("xgxg", 100, "AK47", "男", 10)
T = Terrorist("her", 50, "菜刀", "女", 5)

P.attack(T)
print(T.life)
T.attack(P)
print(P.life)
P2.attack(P)

