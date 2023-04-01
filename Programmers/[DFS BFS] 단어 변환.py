def solution(begin, target, words):
    global Min
    N = len(begin)  # 단어 길이
    M = len(words)  # 단어 개수
    used = [0]*M

    # 다른 알파벳 개수가 한 개인지 확인하는 함수
    def check(w1, w2):
        cnt = 0
        for i in range(N):
            if w1[i] != w2[i]:
                cnt += 1
        if cnt == 1:
            return 1
        else:
            return 0
    Min = 21e8
    def dfs(word, cnt):
        global Min
        if word == target:  # word가 target과 같아지면 cnt 갱신
            Min = min(Min, cnt)
            return
        for i in range(M):  # 모든 단어 배열 돌며
            if used[i] == 0:  # 아직 확인하지 않은 단어이고
                if check(word, words[i]):  # 다른 글자수가 한개이면
                    used[i] = 1
                    dfs(words[i], cnt + 1)  # dfs 탐색
                    used[i] = 0

    dfs(begin, 0)

    if Min == 21e8:  # Min이 21e8이면 탐색 실패한 것
        answer = 0
    else:
        answer = Min

    return answer