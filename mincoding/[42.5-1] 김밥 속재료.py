# 중복 조합

picnic = list(input())
N = len(picnic)
path = [0]*3

def dfs(level, start):
    if level == 3:
        for a in path:
            print(a, end='')
        print()
        return
    for i in range(start, N):
        path[level] = picnic[i]
        dfs(level+1, i)
        path[level] = 0

dfs(0, 0)