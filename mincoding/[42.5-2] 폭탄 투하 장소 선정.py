map = [list(input()) for _ in range(4)]
N = int(input())

# 기준 좌표 주위 4방향 탐색하며 폭탄 터뜨리는 함수
def bomb(y, x):
    temp = []  # 폭탄이 터지는 곳 담을 리스트
    cnt = 0  # 터뜨린 적군 수
    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if 0 <= dy < 4 and 0 <= dx < 4:  # 범위 확인
            if used[dy][dx] == 0 and map[dy][dx] != '_':  # 아직 확인 안한 곳이고 알파벳 적군이 있으면
                used[dy][dx] = 1  # used 배열에 체크하고
                cnt += 1  # cnt + 1
                temp.append([dy, dx])  # 터뜨린 지역 저장
    region.append(temp)  # 최종 터뜨린 지역들을 저장
    return cnt  # 터뜨린 적군 수 리턴


used = [[0]*4 for _ in range(4)]
path = [0]*N  # 폭탄 투하 위치 담을 리스트
Max = 0
region = []
def dfs(level, cnt):
    global Max, answer, region
    if level == N:  # 적군 전부 터뜨리면
        if Max < cnt:  # 적군 수 확인하고 최댓값, 답 갱신
            Max = cnt
            answer = path[:]
        return
    for i in range(4):
        for j in range(4):  # 배열 전부 탐색하고
            if used[i][j] == 0 and map[i][j] != '_':  # 아직 확인 안한 알파벳 적군이면
                used[i][j] = 1  # 방문 체크하고
                path[level] = map[i][j]  # 폭탄 투하 위치 담기
                dfs(level+1, cnt + bomb(i, j) + 1)
                used[i][j] = 0  # 리턴시 방문 체크 해제
                path[level] = 0
                a = region.pop(-1)  # 함께 피해 봤던 4방향도 방문체크 해제
                for b in a:
                    used[b[0]][b[1]] = 0

dfs(0, 0)
answer.sort()  # 오름차순 정렬하고 출력하기
print(*answer)