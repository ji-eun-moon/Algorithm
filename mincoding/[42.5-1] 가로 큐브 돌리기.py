import copy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# cube y행을 오른쪽으로 m칸 이동
def rot(cube, y, m):
    for i in range(N):
        cube[y][(i+m)%N] = arr[y][i]

# 점수 계산하기
def calc(arr):
    score = 1
    for j in range(N):
        Sum = 0
        for i in range(N):
            Sum += arr[i][j]
        score *= Sum

    return score

# cnt 배열 = 회전 횟수 조합
# level : 행 번호 / 저장된 값 : 회전 수
Max = 0
cnt = [0]*N
def dfs(level):
    global Max
    if level == N:
        cube = copy.deepcopy(arr)
        for i in range(N):
            rot(cube, i, cnt[i])
        Max = max(Max, calc(cube))
        return
    for i in range(N):
        cnt[level] = i
        dfs(level+1)
        cnt[level] = 0

dfs(0)

print(f'{Max}점')