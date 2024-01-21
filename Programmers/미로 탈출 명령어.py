import sys
sys.setrecursionlimit(10**8)
def solution(n, m, x, y, r, c, k):

    # 사전 순으로 출발하도록
    directions = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    answer = 'z'

    def dfs(cy, cx, path, cnt):
        nonlocal answer

        # 현재 거리가 목표 지점에서 멀어진 경우
        if cnt + abs(cy-c) + abs(cx-r) > k:
            return

        # k 보다 더 많이 이동한 경우
        if cnt > k:
            return

        if cnt == k:
            if cx == r and cy == c:
                answer = path
                return answer

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 1 <= ny <= m and 1 <= nx <= n:
                if path < answer:
                    if dfs(ny, nx, path + directions[i], cnt + 1):
                        return answer

    # 탈출 불가능 조건
    # 1. k가 최단 거리보다 작은 경우
    # 2. 좌표에 도착할 수 있는 횟수는 최소 거리 + 2의 배수 씩 증가 ****** 31번 테스트케이스
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k-dist) % 2 == 1:
        return 'impossible'

    dfs(y, x, "", 0)

    if answer == 'z':
        return 'impossible'

    return answer

print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))