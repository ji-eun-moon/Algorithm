N = int(input())
num = list(range(1, 10))
cnt = 0
def dfs(level, a):
    global cnt
    if level == N:
        if a == 0:
            cnt += 1
            return
        else:
            return
    if a < 0:
        return
    for i in range(9):
        dfs(level+1, a-num[i])

dfs(0, 10)
print(cnt)