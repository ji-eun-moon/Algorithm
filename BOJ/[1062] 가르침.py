import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 단어 개수, 사용할 수 있는 알파벳 수
words = set(input().rstrip()[4:-4] for _ in range(N))

# anta로 시작하고 tica로 끝나므로 최소로 필요한 단어 수는 5개 (a, c, i, n, t)
# K 가 5보다 작으면 어떤 언어도 배울 수 없음
if K < 5:
    print(0)
    exit()
# K 가 26이면 모든 언어를 배울 수 있음
elif K == 26:
    print(N)
    exit()

# a, c, i, n, t를 제외한 26개 중 K-5 개의 알파벳 뽑기 (조합)
# 해당 조합으로 단어를 만들 수 있는지 확인하여 개수 세기
def dfs(idx, level):
    global Max
    if level == K-5:  # 알파벳 다 뽑았으면
        # 만들 수 있는 단어 최대 개수 확인하기
        cnt = 0
        for word in words:
            for w in set(word).difference('a', 'c', 'i', 'n', 't'):
                if DAT[ord(w) - ord('a')] == 0:
                    break
            else:
                cnt += 1
        Max = max(Max, cnt)
        return

    # 알파벳 뽑기 - 조합
    for i in range(idx, 26):
        if DAT[i] == 0:
            DAT[i] = 1
            dfs(idx+1, level+1)
            DAT[i] = 0

DAT = [0]*26
for c in ('a', 'c', 'i', 'n', 't'):
    DAT[ord(c)-ord('a')] = 1

Max = 0
dfs(0, 0)
print(Max)