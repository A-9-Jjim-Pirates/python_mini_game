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


# 직업이랑 개네들 특수 능력 하기.
class Archer(Hero):     # 궁수
    def hero_magic_attack(self, other, critical_shot):  # other = 공격대상
        super().hero_magic_attack(other)
        self.critical_shot = critical_shot    # 패시브 / 크리티컬 확률 증가

    def critical_shot(self, other):    # 얘는 또 other이 연동 된다..?
        self.mana -= 1
        damage = random.randint(self.mana - 2, self.mana + 2)
        damage = max(0, damage - self.mana)
        other.hp = max(other.hp - damage, 0)


class SwordMan(Hero):     # 전사
    def hero_magic_attack(self, other, iron_body):
        super().hero_magic_attack(other)
        self.iron_body = iron_body     # 자신의 방어력과 최대 HP를 일정 비율 증가시키고, 적에게 피격 시 받는 데미지가 감소

    def iron_body(self, other):    # other이 왜 연동이 안될까..?
        self.mana -= 1
        damage = random.randint(self.mana - 2, self.mana + 2)
        damage = max(0, damage - self.mana)
        damage += random.randint(self.power - 1, self.power + 4)
        self.hp = max(self.hp - self.mana, 0)


class Wizard(Hero):     # 마법사
    def hero_magic_attack(self, other, energy_bolt):
        super().hero_magic_attack(other)
        self.energy_bolt = energy_bolt   # MP를 소비하여 적에게 닿으면 폭발하는 에너지 응집체를 발사

    def iron_body(self, other):     # other이 왜 연동이 안될까..?
        self.mana -= 1
        damage = random.randint(self.mana - 2, self.mana + 2)
        damage = max(0, damage - self.mana)
        damage += random.randint(self.power - 1, self.power + 4)
        self.hp = max(self.hp - self.mana, 0)


class Monster():
    pass
