import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 강의 수, 블루레이 개수
lst = list(map(int, input().split()))  # 강의 길이

Min = max(lst)  # 블루레이 한개의 최소 길이 - 가장 긴 동영상의 길이
Max = sum(lst)  # 블루레이 한개의 최대 길이 - 동영상 길이의 총 합

while Min <= Max:
    mid = (Min+Max) // 2  # 블루레이의 길이 - 중앙 값
    cnt = 1  # 블루레이 개수 - 1개부터 시작
    bluray = 0
    for i in range(N):
        if bluray + lst[i] > mid:  # 담을 수 있는 양을 초과하면
            bluray = lst[i]  # 다음 블루레이로 교체 - 다음 블루레이의 시작점은 초과한 블루레이부터
            cnt += 1  # 블루레이 개수 + 1
        else:  # 초과하지 않으면 (담을 수 있으면) 담기
            bluray += lst[i]

    if cnt > M:  # M보다 더 많은 블루레이가 필요하면 최소값 증가시키기
        Min = mid + 1
    else:  # 그렇지 않으면 최대값 줄여보기
        Max = mid - 1

print(Min)

