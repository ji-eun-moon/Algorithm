players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

from collections import deque
def solution(players, callings):

    player_score = {player: idx for idx, player in enumerate(players, start=1)}  # 선수 : 등수 딕셔너리
    score_player = {idx: player for idx, player in enumerate(players, start=1)}  # 등수 : 선수 딕셔너리

    q = deque(callings)
    while q:
        win = q.popleft()
        idx = player_score[win]
        lose = score_player[idx-1]

        # 등수 : 선수 딕셔너리 갱신
        score_player[idx-1] = win
        score_player[idx] = lose

        # 선수 : 등수 딕셔너리 갱신
        player_score[win] -= 1
        player_score[lose] += 1

    answer = [player for player in score_player.values()]

    return answer

print(solution(players, callings))