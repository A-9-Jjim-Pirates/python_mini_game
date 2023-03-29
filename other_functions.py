from characters import *
import os
import time

# 3초 시간지연


def time_sleep():
    message = "..."
    for i in message:
        print(i)
        time.sleep(1)


def input_hero_name() -> str:
    hero_name = input('이름을 입력해 주세요:')
    if not hero_name:
        hero_name = "Hero"  # 사용자가 이름을 입력하지 않으면 default값으로 "Hero"를 사용한다.
    return hero_name

# 직업선택


def hero_make(name: str, class_dict: dict):
    print('직업목록: 1. Archer  2. Warrior  3. Wizard')
    hero_job_number = input('직업의 번호를 입력해 주세요.: ')

    while True:

        if hero_job_number == "1":
            print('1. Archer를 선택하셨습니다.')
            player_entity = 'A'
            break
        elif hero_job_number == "2":
            print('2. Warrior를 선택하셨습니다.')
            player_entity = 'S'
            break
        elif hero_job_number == "3":
            print('3. Wizard를 선택하셨습니다.')
            player_entity = 'W'
            break
        else:
            print('1, 2, 3 중 선택하여 입력해 주세요.')

    # player_entity = Archer(...)
    return player_entity

# 몬스터의 이름을 랜덤으로 출력


def random_name(self):
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


def before_enter_battle(player_name: str):
    print('던전에 입장합니다.')
    print("마음의 준비를 하세요")

    # 1. 전투시 3:3 화면 표시
    print(f'{player_name}님, 동료1, 동료2 vs 몬스터들 배틀을 시작합니다.')

# hp, mp

# 2. 플레이어 캐리턱의 공격선택(마법? 일반?)

# 3. 클리어 올


def clear_all():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# 전투 종료
print("전투 종료!")
clear_all()
# 보상 뿌리는 화면

print("")

# def choice1():
#     pass
# def choice2():
#     pass
# 상점 만들기


def market():
    print("어서 오세요! 던전 마켓에 오신 것을 환영합니다!")
    print("사고 싶은 물건의 번호를 입력해주세요!")
    print("1 : 체력 회복 물약(5코인), 2 : 마나 회복 물약(5코인)")
    market_list = []
    hero_choice = input("살 물건의 번호를 입력해주세요:")  # 1
    market_list.append(hero_choice)
    # choice_dict={'1':choice1,'2':choice2}
    # choice_dict[hero_choice]() # choice1()
    if "1" in market_list:
        player.mana = max_mana
        player.coin -= 5
        time_sleep()
        print("체력이 FULL입니다!")

    if "2" in market_list:
        player.hp = max_hp
        player.coin -= 5
        time_sleep()
        print("체력이 FULL입니다!")

    else:
        print("다음 스테이지로 넘어갑니다")
        time_sleep()
        clear_all()

