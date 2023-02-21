G, S = map(int, input().split())  # 블록 가로, 세로 길이
N = int(input())  # 상점 개수

lst = []
for _ in range(N):
    p, x = map(int, input().split())  # 상점 위치
    lst.append((p, x))

P, X = map(int, input().split())  # 동근이 위치 (방향, 왼 or 위로부터의 거리)

answer = 0
for a in lst:
    if P == a[0]:  # 방향 같으면
        answer += abs(a[1]-X)
    elif (P == 1 and a[0] == 2) or (P == 2 and a[0] == 1):  # 북-남
        d1 = S + a[1] + X
        d2 = S + (G-a[1]) + (G-X)
        answer += min(d1, d2)
    elif (P == 3 and a[0] == 4) or (P == 4 and a[0] == 3):  # 동-서
        d1 = G + a[1] + X
        d2 = G + (S - a[1]) + (S - X)
        answer += min(d1, d2)
    else:  # 나머지
        if P == 1:  # 북
            if a[0] == 3:  # 서
                answer += (X + a[1])
            elif a[0] == 4:  # 동
                answer += (G-X + a[1])
        elif P == 2:  # 남
            if a[0] == 3:  # 서
                answer += (X + S-a[1])
            elif a[0] == 4:  # 동
                answer += (G-X + S-a[1])
        elif P == 3:  # 서
            if a[0] == 1:  # 북
                answer += (X + a[1])
            elif a[0] == 2:  # 남
                answer += (S-X+a[1])
        elif P == 4:  # 동
            if a[0] == 1:  # 북
                answer += (X + G-a[1])
            elif a[0] == 2:  # 남
                answer += (G-a[1] + S-X)

print(answer)