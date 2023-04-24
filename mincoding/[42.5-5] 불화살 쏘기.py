N = int(input())
lst = list(map(int, input().split()))
used = [0]*N
Max = 0
def fire(idx):
    direct = [-1, 0, 1]
    for i in range(3):
        d = idx + direct[i]
        if 0 <= d < N and used[d] == 0:
            used[d] = 1

def dfs(level, Sum, result):
    global Max, used, ans
    backup = used[:]
    if level == N:
        return
    if Max < Sum:
        ans = result[1:]
        Max = Sum
    for i in range(N):
        if used[i] == 0:
            fire(i)
            dfs(level+1, Sum + lst[i], result+'+'+str(lst[i]))
            used = backup[:]

dfs(0, 0, '')
print(f'{ans}={Max}')
