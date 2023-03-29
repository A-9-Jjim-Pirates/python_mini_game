from characters import *
from battle_management import *
from other_functions import *

# 내 이름 짓기
player_name = input_hero_name()

# 화면전환

# 내 직업 정해서 캐릭터 만들기
hero_entities = []
hero_entities[0] = hero_make(player_name)
# 화면 전환

# 동료 캐릭터 정하기
hero_entities[1] = hero_make('동료1')
hero_entities[2] = hero_make('동료2')
# 화면 전환

# 던전 입장(화면 전환)

# 전투 시작(3회 반복)
# 전투 상황 객체 만들기

for i in range(3):
    battle = BattleScene(hero_entities)

# 전투 상황 객체 안의 함수가 작동되면서 전투가 진행됨


# 전투의 결과 반환
# 패배했으면 게임 끝
# 승리했으면 계속 진행

# 반복문 종료

# 보스전 시작: 전투상황 객체에서 기존과 다른 함수 하나 실행(보스전 전용)
# 전투의 결과 반환
# 패배했으면 게임 끝()
# 승리했으면 게임 끝(해피엔딩 화면)
