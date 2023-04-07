N = int(input())
lst = list(map(int, input().split()))

def cal(a, b, n):
    if n == 0:
        return (a-b)*(a+b)
    elif n == 1:
        return max(a, b)
    elif n == 2:
        return a**2 - b**2
    else:
        return (a+b)**2

# 담긴 경우의 수에 따라 계산하기
def solve():
    num = lst[:]
    for i in range(len(path)):
        a = num.pop(0)  # a, b 를 차례대로 꺼내고
        b = num.pop(0)
        ret = cal(a, b, path[i])  # 계산한 뒤
        num.insert(0, ret)  # 다시 맨 앞에 넣기
    return num[0]

# 연산자 경우의 수 담을 path
path = [0]*(N-1)
cnt = 0
# dfs 중복 순열 사용해서 연산자 사용할수 있는 모든 경우의 수 path에 담기
def dfs(level):
    global cnt
    if level == N-1:
        # 계산 결과가 100이면 return
        if solve() == 100:
            cnt += 1
        return
    for i in range(4):
        path[level] = i
        dfs(level+1)
        path[level] = 0

dfs(0)
print(cnt)