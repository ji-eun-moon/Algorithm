# 톱니바퀴 4개 정보
N = 4
gears = {}
top = [0]*(N+1)  # 12시 방향 인덱스
for i in range(1, N+1):
    gears[i] = list(map(int, input()))

K = int(input())
for _ in range(K):
    idx, dr = map(int, input().split())  # 톱니바퀴 번호, 회전 방향
    lst = [(idx, 0)]  # 회전 시켜야하는 톱니 리스트 (톱니, 같은 방향)
    # 우측 방향 처리
    for i in range(idx+1, N+1):
        # 현재 톱니의 3시 극성과 오른쪽 톱니의 9시 극성이 같지 않을 경우
        if gears[i-1][(top[i-1]+2)%8] != gears[i][(top[i]+6)%8]:
            # 회전 후보에 추가
            lst.append((i, (i-idx)%2))
        else:  # 같은 극성 나오면 종료
            break
    # 왼쪽 방향 처리
    for i in range(idx-1, 0, -1):
        # 현재 톱니의 9시 극성과 왼쪽 톱니의 3시 극성이 같지 않을 경우
        if gears[i][(top[i]+2)%8] != gears[i+1][(top[i+1]+6)%8]:
            # 회전 후보에 추가
            lst.append((i, (idx-i)%2))
        else:  # 같은 극성 나오면 종료
            break

    # 실제 회전 처리
    # dr이 반시계(-1)인 경우 현재 top의 오른쪽(+1)에 위치한 인덱스가,
    # dr이 시계(+1)인 경우 현재 top의 왼쪽(-1)에 위치한 인덱스가 새로운 top이 된다.
    for i, rot in lst:
        # idx 톱니와 같은 방향 회전인 경우
        if rot == 0:
            top[i] = (top[i]-dr) % 8
        else:
            top[i] = (top[i]+dr) % 8


# 점수 계산
answer = 0
score = [0, 1, 2, 4, 8]
for i in range(1, N+1):
    answer += gears[i][top[i]]*score[i]

print(answer)