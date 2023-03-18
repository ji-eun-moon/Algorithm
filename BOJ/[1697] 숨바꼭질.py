N, K = map(int, input().split())
visited = [0]*1000001
def bfs(st):
    global ans
    q = []
    q.append(st)
    visited[st] = 1
    while q:
        x = q.pop(0)
        move = [-1, 1, x]
        for i in range(3):
            dx = x + move[i]
            if 0 <= dx < 100001:
                if visited[dx] == 0:
                    visited[dx] = visited[x] + 1
                    q.append(dx)
                if dx == K:
                    # 시작할때 1 더하고 시작하므로 답은 1 빼야함
                    ans = visited[dx] - 1
                    return ans

bfs(N)
print(ans)