from characters import *
from other_functions import *
monster_wikipedia = [
    {'monster_class_name': 'slime', 'hp': 50,
        'power': 10, 'magic_power': 10, 'agility': 10},
    {'monster_class_name': 'goblin', 'hp': 100,
        'power': 100, 'magic_power': 10, 'agility': 100}
]


class BattleScene:
    def __init__(self, hero_list) -> None:
        self.hero_list = hero_list
        self.monster_list = self.battle_scence_make_monsters()
        move_queue = []
        reward = {}

    def battle_scence_make_monsters(self):
        maden_monster_dict = {}

        for i in range(1, 4):
            monster = random.choice(monster_wikipedia).copy()
            for key_ in monster.keys():
                if key_ == 'monster_class_name':
                    continue
                original = monster[key_]
                adjustment_level = int(original*0.1)
                monster[key_] += random.randint(-1 *
                                                adjustment_level, adjustment_level)
            maden_monster_dict[str(i)] = Monster(**monster)
            # {'1':Monster(name=goblin...),'2':Monster(name=asdf,...)}
        return maden_monster_dict

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
                behavior_dict = {'A': character.attack,
                                 'B': character.hero_magic_attack}
                player_input = foo1(behavior_dict)  # 일반/마법 공격타입 선택 문장 출력
                select_enemy = foo2(self.monster_list)  # 공격할 적 선택 문장 출력
                behavior_dict[player_input](select_enemy)
                # 마법 혹은 공격 후에
                self.battle_scene_check_del_entity(select_enemy)

            for monster in self.monster_list.keys():
                target = random.choice(self.hero_list)
                monster.attack()
                self.battle_scene_check_del_entity(target)
