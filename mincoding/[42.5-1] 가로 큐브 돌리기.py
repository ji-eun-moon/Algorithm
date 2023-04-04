import copy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# y 행을 가로로 N번 회전 시키기
def rot(y, N):
    for _ in range(N):
        lst = arr[y][:]
        for i in range(N):
            cube[y][(i+1)%N] = lst[i]

# 점수 계산하기
def calc(arr):
    lst = []
    for j in range(N):
        Sum = 0
        for i in range(N):
            Sum += arr[i][j]
        lst.append(Sum)
    score = 1
    for num in lst:
        score *= num
    return score

# 가능한 회전 횟수 조합 만들기
result = []
path = [0]*N
def dfs(level):
    global Max
    if level == N:
        result.append(path[:])
        return
    for i in range(N):
        path[level] = i
        dfs(level+1)
        path[level] = 0
dfs(0)

Max = 0
for a in result:
    cube = copy.deepcopy(arr)
    for i in range(N):
        rot(i, a[i])
    Max = max(Max, calc(cube))

print(f'{Max}점')