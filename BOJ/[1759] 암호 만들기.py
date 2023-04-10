L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
path = [0]*L
vowel = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")
def dfs(level, start):
    if level == L:
        cnt1, cnt2 = 0, 0
        for p in path:
            if p in vowel:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            for p in path:
                print(p, end='')
            print()
        return
    for i in range(start, C):
        path[level] = lst[i]
        dfs(level+1, i+1)
        path[level] = 0

dfs(0, 0)