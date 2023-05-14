N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

def binary(st, ed, arr, target):
    if st > ed:
        return 0
    mid = (st+ed)//2
    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return binary(mid+1, ed, arr, target)
    else:
        return binary(st, mid-1, arr, target)

for b in B:
    print(binary(0, N-1, A, b))