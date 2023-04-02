# 직사각형
rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
# 초기 캐릭터 위치
characterX = 1
characterY = 3
# 아이템 위치
itemX = 7
itemY = 8

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 104
    arr = [[0] * N for _ in range(N)]

    # 사각형 칠하기
    for rec in rectangle:
        x1, y1, x2, y2 = rec
        for i in range(y1 * 2, y2 * 2 + 1):
            for j in range(x1 * 2, x2 * 2 + 1):
                arr[i][j] = 1

    # 사각형 내부 0으로 바꾸기
    for rec in rectangle:
        x1, y1, x2, y2 = rec
        for i in range(y1 * 2 + 1, y2 * 2):
            for j in range(x1 * 2 + 1, x2 * 2):
                arr[i][j] = 0

    used = [[0] * N for _ in range(N)]
    Min = 21e8

    def bfs():
        direct_y = [-1, 1, 0, 0]
        direct_x = [0, 0, -1, 1]
        q = []
        q.append((characterY * 2, characterX * 2))
        used[characterY * 2][characterX * 2] = 1
        while q:
            y, x = q.pop(0)
            if y == itemY * 2 and x == itemX * 2:
                return used[y][x] // 2
            for i in range(4):
                dy = y + direct_y[i]
                dx = x + direct_x[i]
                if 0 <= dy < N and 0 <= dx < N:
                    if used[dy][dx] == 0 and arr[dy][dx] == 1:
                        used[dy][dx] = used[y][x] + 1
                        q.append((dy, dx))
    answer = bfs()
    return answer

print(solution(rectangle, characterX, characterY, itemX, itemY))