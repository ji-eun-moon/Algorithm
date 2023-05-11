from heapq import heappush, heappop, heapify

N = int(input())

golds = list(map(int, input().split()))
golds = [[gold, 0] for gold in golds]
heapify(golds)

def check(golds):
    cnt = 0
    while golds:
        for _ in range(2):
            a = heappop(golds)
            if a[1] == 1:
                return cnt
            cnt += 1
        heappush(golds, [a[0]*2, 1])

print(check(golds))