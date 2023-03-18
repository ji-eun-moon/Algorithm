N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 아무 지역도 물에 잠기지 않을 때 답은 1 -> 최댓값
Max = 1
direct_y = [-1, 1, 0, 0]
direct_x = [0, 0, -1, 1]
# 안전영역의 크기를 cnt하는 bfs 함수
def bfs(y, x):
    cnt = 0
    q = []
    q.append((y, x))
    while q:
        cnt += 1
        y, x = q.pop(0)
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] > rain and visited[dy][dx] == 0:
                    visited[dy][dx] = 1
                    q.append((dy, dx))
    return cnt


# 높이가 1~100이므로 1~100 확인
rain = 1
while True:
    if rain == 100:
        break
    # 반복문 수행할 때마다 visit 배열 초기화
    visited = [[0]*N for _ in range(N)]
    result = []
    for y in range(N):
        for x in range(N):
            # 안전지역이고 방문한적 없으면 안전지역 크기 확인
            if arr[y][x] > rain and visited[y][x] == 0:
                visited[y][x] = 1
                # 해당 안전지역 크기 담기
                result.append(bfs(y, x))
    # result의 길이 = 안전지역의 개수
    Max = max(Max, len(result))
    rain += 1

print(Max)