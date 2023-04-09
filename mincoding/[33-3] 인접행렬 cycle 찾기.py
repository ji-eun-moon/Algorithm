N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

root = [0]*N

def findboss(member):
    if root[member] == 0:
        return member
    ret = findboss(root[member])
    root[member] = ret
    return ret

def setunion(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    root[fb] = fa

result = '미발견'
for i in range(N):
    for j in range(N):
        if i >= j and arr[i][j] == 1:
            ret = setunion(i, j)
            if ret == 1:
                result = 'cycle 발견'


print(result)