price = {'a': 15, 'b': 20, 'c': 44, 'd': 22, 'e': 55, 'f': 16, 'g': 45}

item = list(input())
N = len(item)  # item 개수
e = int(input())  # 제외할 item 개수
Max = 0
used = [0]*N
def dfs(level, Sum):
    global Max
    if level == N-e:
        if Max < Sum and Sum % 10 == 0:
            Max = Sum
        return
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            dfs(level+1, Sum + price[item[i]])
            used[i] = 0
dfs(0, 0)
print(Max)