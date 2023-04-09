N = int(input())
edge = []
for _ in range(N):
    edge.append(input().split())

arr = [0]*200
def findboss(member):
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return arr[ord(member)]

def setunion(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    arr[ord(fb)] = fa

answer = '미발견'
for i in range(N):
    a, b = edge[i]
    if setunion(a, b):
        answer = '발견'

print(answer)