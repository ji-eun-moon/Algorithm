lst = list(input())
N = int(input())
M = len(lst)
def score(word):
    result = 0
    for i in range(1, M):
        if word[i] == word[i-1]:
            result -= 50
        elif abs(ord(word[i])-ord(word[i-1])) <= 5:
            result += 3
        elif abs(ord(word[i])-ord(word[i-1])) >= 20:
            result += 10
    return result

Max = 0
def dfs(level):
    global Max
    if level == N:
        Max = max(Max, score(lst))
        return
    for i in range(M-1):
        for j in range(i+1, M):
            lst[i], lst[j] = lst[j], lst[i]
            dfs(level+1)
            lst[i], lst[j] = lst[j], lst[i]

dfs(0)
print(Max)