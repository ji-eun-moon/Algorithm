N = int(input())
arr = [list(input()) for _ in range(N)]
hang = list(zip(*arr))[0]  # 행 번호 찾기 위해서 각 리스트의 0번 인덱스만 묶은 것
def binary(arr, st, ed):
    if st > ed:
        return st - 1
    mid = (st + ed) // 2
    if arr[mid] == '#':
        return binary(arr, mid + 1, ed)
    elif arr[mid] == '0':
        return binary(arr, st, mid - 1)

y = binary(hang, 0, N-1)
x = binary(arr[y], 0, N-1)
print(y, x)