from characters import *
import os
import time
tab = '\t'
notab = ''
# hp, power, magic_power, agility, mana


# 클리어 올


def clear_all():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# 3초 시간지연


def time_sleep():
    message = "..."
    for i in message:
        print(i, end="")
        time.sleep(0.5)
    print()
# 히어로 이름 짓는 함수


def input_hero_name() -> str:
    while True:
        hero_name = input('이름을 입력해 주세요:')
        if len(hero_name) > 8:
            print('8글자 이내로 정해주세요')
            time.sleep(2)
            clear_all()
            continue
        if not hero_name:
            hero_name = "Hero"
        break  # 사용자가 이름을 입력하지 않으면 default값으로 "Hero"를 사용한다.
    return hero_name

# 직업선택


def hero_make(name: str, class_dict: dict):

    while True:
        print(f'{name}의 직업을 정하기')
        print('직업목록: 1. Archer  2. Swordsman  3. Wizard')
        hero_job_number = input('직업의 번호를 입력해 주세요.: ')
        if hero_job_number == "1":
            print('1. Archer를 선택하셨습니다.')
            class_key = 'A'
            break
        elif hero_job_number == "2":
            print('2. Swordsman를 선택하셨습니다.')
            class_key = 'S'
            break
        elif hero_job_number == "3":
            print('3. Wizard를 선택하셨습니다.')
            class_key = 'W'
            break
        else:
            print('1, 2, 3 중 선택하여 입력해 주세요.')
            time.sleep(2)
            clear_all()
    info_dict = class_status_wikipedia[class_key]
    info_dict['name'] = name
    time.sleep(2)
    clear_all()
    return class_dict[class_key](**info_dict)

# 몬스터의 이름을 랜덤으로 출력


def random_name():
    vowel = 'aeiou'
    non_vowel = 'bcdfghjklmnpqrstvwxyz'
    name = ''
    name = name+chr(random.randint(65, 90))
    for i in range(random.randint(1, 2)):
        name = name + vowel[random.randint(0, 4)]
    for i in range(random.randint(1, 3)):
        name = name + non_vowel[random.randint(0, 10)]
    name = name+vowel[random.randint(0, 4)]
    name = name + non_vowel[random.randint(0, 10)]
    return name


# 던전 드가는 화면 표시
def before_enter_battle(hero_list: dict, monster_list: dict):
    print('다음 층으로 입장합니다... 전투 시작!')
    print("마음의 준비를 하세요!")

    # 1. 전투시 3:3 화면 표시
    print('========== Heros \t   vs   \t Monsters ==========')
    for i in range(1, 4):
        hero = hero_list.get(str(i))
        hero_name = str(hero.name if hero else '---')
        print(
            f"\t\t{hero_name}\t\t{tab if len(hero_name)<8 else notab}{monster_list.get(str(i)).monster_class_name}")
    input('press enter to move on')
    clear_all()

# hp, mp 출력


def check_hero_and_monster_status(hero_list: dict, monster_list: dict):
    print('================================================')
    print('| Heroes\t| HP\t\t| Mana\t\t|')

    for entity in hero_list.values():
        show_hp, show_mana = entity.hero_check_status()
        print(
            f'| {entity.name}\t{tab if len(entity.name)<6 else notab}| {show_hp}\t| {show_mana}\t|')
    print('================================================')
    print('=================================')
    print('|Monsters\t|HP\t\t|')
    for monster_entity in monster_list.values():
        monster_show_hp = monster_entity.check_status()
        print(
            f'| {monster_entity.name}\t{tab if len(monster_entity.name)<6 else notab}| {monster_show_hp}\t|')
    print('=================================')


# 2. 플레이어 캐리턱의 공격선택하는 함수(마법? 일반?)(foo1)


def hero_attack_select(hero_name, behavior_dict: dict):

    print("일반공격: 1, 마법공격: 2")

    while True:
        attack_type = input(f"{hero_name}님! 어떤 공격을 하시겠습니까?: ")
        if attack_type not in behavior_dict.keys():
            print('1, 2 중 선택하여 다시 입력해 주세요')
            time.sleep(2)
        else:
            return attack_type

# 공격할 몬스터 선택하는 함수(foo2)> str반환


def select_monster(hero_name, monster_list: dict):
    for key_, entity in monster_list.items():
        print(f"{key_}:{entity.name} the {entity.monster_class_name}")

    while True:
        monster_number = input(
            f"{hero_name}님! 공격할 몬스터를 선택하세요{list(monster_list.keys())} : ")
        if monster_number not in monster_list.keys():
            print(f"{list(monster_list.keys())} 중에서 선택하여 입력해 주세요.")
            continue
        else:
            clear_all()
            return monster_number


# 전투 종료
def choice_play_or_exit(is_game_over):
    print(f"GAME {'OVER' if is_game_over else 'WIN'}!!!")
    dictionary = {'y': True, 'n': False}
    while True:
        game_over_answer = input("게임을 종료하시겠습니까?:y/n ")
        if game_over_answer in ['y', 'n']:
            break
        print('y와 n 중 선택하여 다시 입력해 주세요')
    time.sleep(2)
    clear_all()
    return dictionary[game_over_answer]

# 보상 뿌리는 화면


def give_reward():
    time_sleep()
    print("던전 마켓에 입장합니다")
    time_sleep()
# 상점에서 물약 선택하면 마나,체력 회복시키는 함수


def choice_one(hero_list, reward):
    while True:
        print("누가 사먹을까요?")
        for key_, entity in hero_list.items():
            print(f"{key_}:{entity.name} the {entity.__class__.__name__}")
        select = input("숫자로 선택: ")
        if select in hero_list.keys():
            selected_hero = hero_list[select]
            break
        print('다시 입력하세요')

    if reward[0] < 120:
        print(f"돈이 없으므로({reward[0]} G) 다음 라운드로 갑니다")
        time_sleep()
        clear_all()

    else:
        reward[0] -= 120
        selected_hero.mana = selected_hero.max_mana
        selected_hero.hp = selected_hero.max_hp
        print(f"구매에 성공 했습니다! 남은 돈은 {reward[0]} G 입니다")
        time_sleep()
        print("체력과 마나가 전부 채워졌습니다!")
        time_sleep()
        clear_all()

# 상점 만들기


def market(hero_list, reward):
    print("어서 오세요! 던전 마켓에 오신 것을 환영합니다!")

    while True:
        hero_choice = input("파워엘릭서(체력,마나 회복)(120 G)를 구매하시겠습니까?(y/n)")

        if hero_choice == "y":
            choice_one(hero_list, reward)
            break

        elif hero_choice == "n":
            time_sleep()
            break

        else:
            print("올바른 문자를 입력해주세요")
            continue

    print("다음 라운드로 넘어갑니다!")
    time_sleep()
    clear_all()

    # 파워 도박하는 함수
    # def power_gambling(hero_list):
    #   print("당신의 파워가 랜덤으로 증가하거나 감소합니다.")
    #   gambling_choice = input("하시겠습니까? (y/n) : ")
    #   if gambling_choice == "y":
    #       random_number = random.ranint(-10,+10)
    #       hero_list["1"].power += random_number
    #        print(f"{hero_list["1"].name}의 파워가 {random_number} 만큼 증가했습니다!")
    #   else: print("알겠습니다")
    #   print("다음 라운드로 넘어갑니다!")
    #   time_sleep()
