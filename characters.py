import random


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power, magic_power, agility):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.magic_power = magic_power
        self.agility = agility

    def attack(self, other):
        damage = random.randint(int(self.power*0.8), int(self.power*1.2))
        other.hp = max(other.hp - damage, 0)

    def check_status(self):
        pass


class Hero(Character):
    def __init__(self, name, hp, power, magic_power, agility, mana):
        super().__init__(name, hp, power, magic_power, agility)
        self.max_mana = mana
        self.mana = mana

    def hero_magic_attack(self, other):
        damage = random.randint(int(self.magic_power*0.8),
                                int(self.magic_power*1.2))
        other.hp = max(other.hp - damage, 0)

    def hero_mama_check(self, mana_spend):
        if self.mama-mana_spend > 0:
            return True
        else:
            return False

    def hero_check_status(self):
        pass

    def hero_get_reward(self):
        pass


class Archer(Hero):
    def hero_magic_attack(self, other):
        # adfadsf
        super().hero_magic_attack(other)
        # assfsdfsdf


class Monster(Character):
    pass
