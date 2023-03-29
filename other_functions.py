from characters import *
import os


def input_hero_name() -> str:
    input('이름을 입력해 주세요')


def hero_make(name: str):
    print('직업목록')
    a = input('직업을 정하세요: ')
    player_entity = Archer(...)
    return player_entity


def monster_make():

    pass


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

# 1. 전투시 3:3 화면 표시
# hp, mp

# 2. 플레이어 캐리턱의 공격선택(마법? 일반?)

# 3. 클리어 올


def clear_all(self):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# 전투 종료

# 보상 뿌리는 화면
