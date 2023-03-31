from characters import *
from other_functions import *


class BattleScene:
    def __init__(self, hero_list: dict, floor: int) -> None:
        self.hero_list = hero_list
        self.reward = 0
        self.floor = floor
        self.monster_list = self.battle_scence_make_monsters()

    def battle_scence_make_monsters(self):
        monster_entities = {}

        for i in range(1, 4):
            monster = random.choice(monster_wikipedia).copy()
            for key_ in list(monster.keys()):
                if key_ == 'monster_class_name':
                    continue
                # 층계를 오를 수록 몬스터가 조금씩 강해진다
                original = monster[key_] + self.floor * 4
                adjustment_level = int(original*0.1)
                monster[key_] = original+random.randint(-1 *
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
            heroes_agility = 0
            i = 0
            for entity in self.hero_list.values():
                i += 1
                heroes_agility += entity.agility
            heroes_agility = heroes_agility//i

            monsters_agility = 0
            i = 0
            for entity in self.monster_list.values():
                i += 1
                monsters_agility += entity.agility
            monsters_agility = monsters_agility//i

            # 같으면 그냥 플레이어가 우선하게 합시다
            # 비교의 결과에 따라 순서대로 두 함수들을 호출
            heroes_agility = heroes_agility+random.randint(-2, 2)
            monsters_agility = monsters_agility+random.randint(-1, 1)
            print(
                f'플레이어팀의 속도: {heroes_agility}, 몬스터팀의 속도: {monsters_agility}')
            if heroes_agility+random.randint(-2, 2) < monsters_agility:
                print('몬스터가 먼저 공격합니다.')
                self.monster_scene_turn()
                self.hero_scene_turn()
            else:
                print('플레이어가 먼저 공격합니다.')
                self.hero_scene_turn()
                self.monster_scene_turn()
            # 전투종료
        if not self.monster_list:  # victory
            print("=====\n전투 승리!\n=====")  # 전투 승리 화면 출력
            # 레벨업 함수 불러오기
            for entity in self.hero_list.values():
                entity.hero_level_up()  # 전원 레벨업
                input("press enter to progress")
                clear_all()
            return self.reward
        else:
            print("=====\n전투 패배...\n=====")
            return -1

    def hero_scene_turn(self):
        for key_ in list(self.hero_list.keys()):  # 플레이어들의 공격을 진행하는 부분입니다
            if not self.monster_list:  # 몬스터 없으면 바로 종료
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
    def monster_scene_turn(self):
        for key_ in self.monster_list.keys():  # 몬스터들의 공격이 진행되는 부분입니다
            #  플레이어가 모두 죽으면 바로 끝냄
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


class BossBattleScene(BattleScene):
    #  몬스터 생성만 오버라이딩
    def battle_scence_make_monsters(self):
        monster_entities = {}
        monster_entities['1'] = BossMonster()
        monster_entities['2'] = BossMonster()
        monster_entities['3'] = BossMonster()
        return monster_entities
