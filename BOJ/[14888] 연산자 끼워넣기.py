# DFS
N = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())  # 덧셈, 뺄셈, 곱셈, 나눗셈 개수

Min = int(1e9)
Max = -int(1e9)

def dfs(add, sub, mul, div, value, level):
    global Min, Max
    if level == N:
        Min = min(Min, value)
        Max = max(Max, value)
        return
    else:
        if add > 0:
            dfs(add-1, sub, mul, div, value + number[level], level+1)
        if sub > 0:
            dfs(add, sub-1, mul, div, value - number[level], level+1)
        if mul > 0:
            dfs(add, sub, mul-1, div, value * number[level], level+1)
        if div > 0:
            dfs(add, sub, mul, div-1, int(value/number[level]), level+1)

dfs(add, sub, mul, div, number[0], 1)
print(Max)
print(Min)
