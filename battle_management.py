from characters import *
from other_functions import *


class BattleScene:
    def __init__(self, hero_list) -> None:
        self.hero_list = hero_list
        self.monster_list = self.battle_scence_make_monsters()
        move_queue = []
        reward = {}

    def battle_scence_make_monsters(self):
        return {1: Monster(...), 2: Monster(...), 3: Monster(...)}

    def reward_save():
        pass

    def battle_scene_check_del_entity(self, target):
        if target.check_status():
            # 빼기
            True
        else:
            False
            # 넘어가기

    def battle_scence_turn(self):
        while (self.hero_list or self.monster_list):
            for character in self.hero_list:
                input()

                # 마법 혹은 공격 후에
                self.battle_scene_check_del_entity('target')
            for monster in self.monster_list:
                monster.attack(random.choice([1, 2, 3, 4]))
                # 공격 후에
                self.battle_scene_check_del_entity('target')
