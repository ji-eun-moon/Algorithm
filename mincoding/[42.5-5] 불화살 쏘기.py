N = int(input())
lst = list(map(int, input().split()))
used = [0]*N
Max = 0
def fire(idx):
    temp = []
    direct = [-1, 1]
    for i in range(2):
        d = idx + direct[i]
        if 0 <= d < N and used[d] == 0:
            used[d] = 1
            temp.append(d)
    region.append(temp)

region = []
def dfs(level, Sum):
    global Max
    if level == N:
        if Max < Sum:
            Max = Sum
        return
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            fire(i)
            dfs(level+1, Sum + lst[i])
            used[i] = 0
            a = region.pop(-1)
            for b in a:
                used[b] = 0

dfs(0, 0)
print(Max)