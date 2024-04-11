d, n, m = map(int, input().split())  # 탈출구까지의 거리, 작은 돌섬 수, 제거할 수 있는 작은 돌섬 수
islands = [int(input()) for _ in range(n)]  # island[i] = 갇힌 섬으로부터 돌섬 i 까지의 거리
islands.append(d)
islands.sort()
start, end = 0, d
answer = 0

while start <= end:
    mid = (start+end) // 2  # 각 지점 사이의 거리의 최솟값
    Min = float('inf')
    remove = 0
    current = 0

    for island in islands:
        dist = island - current  # 현재 위치에서 다음 섬 사이의 거리
        if dist < mid:  # mid 보다 거리가 짧으면 제거
            remove += 1
        else:  # mid 보다 길면
            current = island  # 섬 위치 이동
            Min = min(Min, dist)  # 최소 거리 갱신
        if remove > m:
            break

    if remove > m:  # 너무 많이 제거한 경우 mid 줄이기
        end = mid - 1
    else:
        answer = Min
        start = mid + 1

print(answer)