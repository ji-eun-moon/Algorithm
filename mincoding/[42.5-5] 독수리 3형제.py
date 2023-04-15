lst = list(map(int, input().split()))
N = int(input())
Max = 0
def dfs(level, Sum):
    global Max, lst

    if level == N:
        if Max < Sum:
            Max = Sum
        return

    if level > 0:
        lst = list(map(lambda x: x*2, lst))

    backup = lst[:]
    for i in range(3):
        for j in range(3, 6):
            for k in range(1, 5):
                eat = lst[i]
                lst[i] = 0
                eat += lst[j]
                lst[j] = 0
                eat += lst[k]
                lst[k] = 0
                dfs(level+1, Sum + eat)
                lst = backup[:]

dfs(0, 0)
print(Max)