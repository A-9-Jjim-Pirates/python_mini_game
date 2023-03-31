from characters import *
from battle_management import *
from other_functions import *

# 내 이름 짓기


def main():
    clear_all()
    player_name = input_hero_name()
    # 화면전환

    # 내 직업 정해서 캐릭터 만들기
    hero_entities = {}
    list_of_class = list(Hero.__subclasses__())  # [archer,swordman, wizard]
    acrhonym_to_class = {}
    for class_ in list_of_class:
        acrhonym_to_class[class_.__name__[0]] = class_
    hero_entities['1'] = hero_make(player_name, acrhonym_to_class)
    # 화면 전환

    # 동료 캐릭터 정하기
    hero_entities['2'] = hero_make(random_name(), acrhonym_to_class)
    hero_entities['3'] = hero_make(random_name(), acrhonym_to_class)
    # 화면 전환

    # 던전 입장(화면 전환)

    # 전투 시작(수 회 반복)
    total_reward = {0: 0}
    for i in range(5):
        # 전투 상황 객체 만들기
        battle = BattleScene(hero_entities)
        # 전투 상황 객체 안의 함수가 작동되면서 전투가 진행되고 결과(리워드) 반환
        battle_reward = battle.battle_scene_turn()
        print(f"전리품으로 {battle_reward} G를 얻었습니다.")
        total_reward[0] += battle_reward
        print(f"소지금: {total_reward[0]} G")
        # 패배했으면 게임 끝
        if battle_reward == -1:
            if choice_play_or_exit(True):  # gameover_and_retry 화면 출력
                return True  # gameover ,no try again
            return False  # gameover, try again
        give_reward()  # 화면 표시
        market(hero_entities, total_reward)  # 아이템 사기 진입
        # 다음전투로 진행
    # 반복문 종료

    # 보스전 시작: 전투상황 객체에서 기존과 다른 함수 하나 실행(보스전 전용)
    battle = BossBattleScene(hero_entities)
    result = battle.battle_scene_turn()
    if result == -1:
        gameover = True
        if choice_play_or_exit(True):  # gameover_and_retry 화면 출력
            return True  # gameover ,no try again
        return False  # gameover, try again
    total_reward[0] += result
    print("해피엔딩")
    if choice_play_or_exit(False):  # game_win_and_retry 화면 출력
        return True  # win ,no try again
    return False  # win, try again


# 시작
while not main():
    True
