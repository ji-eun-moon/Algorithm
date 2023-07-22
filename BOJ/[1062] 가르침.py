from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 단어 개수, 사용할 수 있는 알파벳 수
words = set(input().rstrip()[4:-4] for _ in range(N))
default = {'a','n','t','i','c'}

# anta로 시작하고 tica로 끝나므로 최소로 필요한 단어 수는 5개 (a, c, i, n, t)
# K 가 5보다 작으면 어떤 언어도 배울 수 없음
if K < 5:
    print(0)
    exit()
# K 가 26이면 모든 언어를 배울 수 있음
elif K == 26:
    print(N)
    exit()

DAT = [0]*123
for c in ('a', 'c', 'i', 'n', 't'):
    DAT[ord(c)] = 1

# a, c, i, n, t를 제외한 26개 중 K-5 개의 알파벳 뽑기 (조합)
# 해당 조합으로 단어를 만들 수 있는지 확인하여 개수 세기
def cntWords():
    cnt = 0
    for word in words:
        for w in word:
            if DAT[ord(w)] == 0:
                break
        else:
            cnt += 1
    return cnt

remain_alphabet = set(chr(i) for i in range(97, 123)) - default
Max = 0

for teach_word in list(combinations(remain_alphabet, K-5)):
    for t in teach_word:
        DAT[ord(t)] = 1

    Max = max(Max, cntWords())

    for t in teach_word:
        DAT[ord(t)] = 0

print(Max)