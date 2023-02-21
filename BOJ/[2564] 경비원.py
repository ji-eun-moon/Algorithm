G, S = map(int, input().split())  # 블록 가로, 세로 길이
N = int(input())  # 상점 개수

lst = []
for _ in range(N):
    p, x = map(int, input().split())  # 상점 위치
    lst.append((p, x))

P, X = map(int, input().split())  # 동근이 위치 (방향, 왼 or 위로부터의 거리)

answer = 0
for a in lst:
    if (a[0], P) == (1, 2) or (a[0], P) == (2, 1):
        d1 = S + X + a[1]
        d2 = S + (G-X) + (G-a[1])
        answer += min(d1, d2)
    elif (a[0], P) == (1, 3) or (a[0], P) == (3, 1):
        answer += (X + a[1])
    elif (a[0], P) == (4, 3) or (a[0], P) == (3, 4):
        d1 = G + X + a[1]
        d2 = G + (S - X) + (S - a[1])
        answer += min(d1, d2)
    elif (a[0], P) == (1, 4):
        answer += (G - a[1] + X)
    elif (a[0], P) == (4, 1):
        answer += (G + a[1] - X)

print(answer)