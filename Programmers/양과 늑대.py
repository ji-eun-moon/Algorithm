def solution(info, edges):
    N = len(info)
    answer = 0

    tree = {i : [] for i in range(N)}
    for p, c in edges:
        tree[p].append(c)

    visited = [0]*N
    def dfs(start, sheep, wolf):
        nonlocal answer

        if wolf >= sheep:
            return

        answer = max(answer, sheep)

        for nxt in tree[start]:
            if not visited[nxt]:
                visited[nxt] = 1
                if info[nxt] == 0:
                    dfs(nxt, sheep+1, wolf)
                else:
                    dfs(nxt, sheep, wolf+1)
                visited[nxt] = 0

    visited[0] = 1
    dfs(0, 1, 0)

    return answer

print('#1', solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print('#2', solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))