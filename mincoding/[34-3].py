N = int(input())
books = list(input().split())

def binary(arr, target, st, ed, cnt):
    if st > ed or cnt > time:
        return 'fail'
    mid = (st + ed)//2
    if arr[mid] == target:
        return 'pass'

M = int(input())
for _ in range(M):
    book, t = input().split()
    time = int(t)
    print(binary(books, book, 0, N, 0))