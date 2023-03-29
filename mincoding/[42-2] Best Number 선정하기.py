num = list(map(int, input().split()))

path = [0]*5
used = [0]*5

Max, Min = 0, 21e8
def dfs(level):
    global Min, Max
    if level == 5:
        ans = (path[0] * path[1]) - (path[2] * path[3]) + path[4]
        Min = min(ans, Min)
        Max = max(ans, Max)
    for i in range(5):
        if used[i] == 0:
            used[i] = 1
            path[level] = num[i]
            dfs(level+1)
            path[level] = 0
            used[i] = 0

dfs(0)
print(Max)
print(Min)