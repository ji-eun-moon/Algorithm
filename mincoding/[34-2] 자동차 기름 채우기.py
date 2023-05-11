lst = list(input())

def binary(arr, st, ed):
    if st > ed:
        return st
    mid = (st + ed) // 2
    if arr[mid] == '#':
        return binary(arr, mid+1, ed)
    elif arr[mid] == '_':
        return binary(arr, st, mid-1)

oil = binary(lst, 0, 10)
print(f'{oil*10}%')