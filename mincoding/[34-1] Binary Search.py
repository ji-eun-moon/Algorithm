arr = [4, 4, 5, 7, 8, 10, 20, 22, 23, 24]

N = int(input())

def binary(arr, num, st, ed):
    if st > ed:
        return 'X'
    mid = (st + ed) // 2
    if arr[mid] == num:
        return 'O'
    elif arr[mid] > num:
        return binary(arr, num, st, mid-1)
    elif arr[mid] < num:
        return binary(arr, num, mid+1, ed)


print(binary(arr, N, 0, len(arr)))

def binary2(arr, num, st, ed):
    while st <= ed:
        mid = (st + ed)//2
        if arr[mid] == num:
            return 'O'
        elif arr[mid] > num:
            ed = mid - 1
        elif arr[mid] < num:
            st = mid + 1
    return 'X'

print(binary2(arr, N, 0, len(arr)))