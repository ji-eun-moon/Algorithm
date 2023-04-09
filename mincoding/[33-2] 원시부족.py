person = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
arr = [0, 'A', 'A', 0, 'D', 'D', 0, 'G', 0, 'I']

def findboss(member):
    if arr[person[member]] == 0:
        return member
    ret = findboss(arr[person[member]])
    arr[person[member]] = ret
    return ret

def setunion(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    arr[person[fb]] = fa

N = int(input())
for _ in range(N):
    a, b = input().split()
    setunion(a, b)

cnt = 0
for i in range(10):
    if arr[i] == 0:
        cnt += 1

print(f'{cnt}개')