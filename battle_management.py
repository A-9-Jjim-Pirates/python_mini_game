from characters import *
from other_functions import *


class BattleScene:
    def __init__(self, hero_list: dict) -> None:
        self.hero_list = hero_list
        self.monster_list = self.battle_scence_make_monsters()
        self.reward = 0

    def battle_scence_make_monsters(self):
        monster_entities = {}

        for i in range(1, 4):
            monster = random.choice(monster_wikipedia).copy()
            for key_ in list(monster.keys()):
                if key_ == 'monster_class_name':
                    continue
                original = monster[key_]
                adjustment_level = int(original*0.1)
                monster[key_] += random.randint(-1 *
                                                adjustment_level, adjustment_level)
            monster['name'] = random_name()
            monster_entities[str(i)] = Monster(**monster)
            # {'1':Monster(monster_class_name=goblin...),'2':Monster(monster_class_name=name=asdf,...)}
        return monster_entities

    def battle_scene_check_del_entity(self, target, entity_list: dict):
        if entity_list[target].hp == 0:
            # 빼기
            print(f"{entity_list[target].name}가 쓰러졌다.")
            corps = entity_list.pop(target, None)  # 키로 찾아서 제거. 없으면 None반환
            return corps
        return None

    def battle_scene_turn(self):
        before_enter_battle(self.hero_list, self.monster_list)
        # 히어로나 몬스터가 모두 죽을 때 까지 반복
        while (self.hero_list and self.monster_list):

            for key_ in list(self.hero_list.keys()):
                if not self.monster_list:
                    break
                check_hero_and_monster_status(
                    self.hero_list, self.monster_list)
                selected_hero = self.hero_list[key_]
                behavior_dict = {'1': selected_hero.attack,
                                 '2': selected_hero.hero_magic_attack}
                player_input = hero_attack_select(
                    selected_hero.name, behavior_dict)  # 일반/마법 공격타입 선택 문장 출력
                # 공격할 적 선택 문장 출력(키를 반환)# {'1':Monster(monster_class_name=goblin...),'2':Monster(monster_class_name=name=asdf,...)}
                select_enemy = select_monster(
                    selected_hero.name, self.monster_list)
                behavior_dict[player_input](self.monster_list[select_enemy])
                # 마법 혹은 공격 후에 적 죽었는지 확인해서 죽었으면 시체 반환
                monster_corp = self.battle_scene_check_del_entity(
                    select_enemy, self.monster_list)
                # 시체에서 돈 털기
                if monster_corp:
                    self.reward += monster_corp.reward
                time.sleep(1)

            # 적 공격 순서
            for key_ in self.monster_list.keys():

                if not self.hero_list:
                    break

                target = random.choice(list(self.hero_list.keys()))
                print('===적의 공격!!!===')
                self.monster_list[key_].attack(self.hero_list[target])
                # 히어로 죽었는지 확인
                self.battle_scene_check_del_entity(target, self.hero_list)
                time.sleep(1)
            time.sleep(1)
            clear_all()

        if not self.monster_list:  # victory
            print("=====\n전투 승리!\n=====")  # 전투 승리 화면 출력
            # 레벨업 함수 불러오기
            for entity in self.hero_list.values():
                entity.hero_level_up()  # 전원 레벨업
            return self.reward
        else:
            print("=====\n전투 패배...\n=====")
            return -1


class BossBattleScene(BattleScene):
    #  몬스터 생성만 오버라이딩
    def battle_scence_make_monsters(self):
        monster_entities = {}
        monster_entities['1'] = BossMonster()
        monster_entities['2'] = BossMonster()
        monster_entities['3'] = BossMonster()
        return monster_entities
