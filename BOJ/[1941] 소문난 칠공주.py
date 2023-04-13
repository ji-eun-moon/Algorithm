from collections import deque

# 학생들 배열
arr = [list(input()) for _ in range(5)]

# 중복순열 - 학생들의 인덱스가 담긴 리스트 만들기
student = []
path = [0]*2
def student_idx(level):
    if level == 2:
        student.append(path[:])
        return
    for i in range(5):
        path[level] = i
        student_idx(level+1)
student_idx(0)

# student 배열에서 7명을 뽑는 조합 만들기
visited = [[0]*5 for _ in range(5)]
princess = [0]*7
ans = 0
def pick(level, start):
    global ans
    if level == 7:
        # 7명 다 뽑았을 때 그 7명이 인접해 있고 다솜파가 4명 이상인지 확인
        if check():
            ans += 1
        return
    for i in range(start, 25):
        princess[level] = student[i]
        y, x = student[i]
        visited[y][x] = 1
        pick(level+1, i+1)
        visited[y][x] = 0

def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                # return bfs(i, j)가 아니라 bfs(i, j)로 하면 전부 탐색해버리기 때문에 오답
                return bfs(i, j)


# bfs - 섬 구했던 방법으로 인접해 있는지 확인하기
# 만약에 섬의 크기가 7이면 전부 인접해 있는 것!
def bfs(y, x):

    used = [[0]*5 for _ in range(5)]

    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]

    q = deque()
    q.append((y, x))
    used[y][x] = 1
    cnt = 1  # 섬 크기
    scnt = 0  # 다솜파 인원
    while q:
        y, x = q.popleft()
        # 만약 다솜파이면 scnt += 1
        if arr[y][x] == 'S':
            scnt += 1
        for i in range(4):  # 상하좌우 탐색하여
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < 5 and 0 <= dx < 5:
                # 아직 방문 안한 곳(used = 0)이고 인접해 있는 곳이면(visited = 1)
                if used[dy][dx] == 0 and visited[dy][dx] == 1:
                    used[dy][dx] = 1
                    cnt += 1  # 공주 크기 + 1
                    q.append((dy, dx))

    # 반복문 종료 되었을때 칠공주이고 다솜파가 4명이상이라면 1리턴
    if cnt == 7 and scnt >= 4:
        return 1
    else:
        return 0

pick(0, 0)
print(ans)
