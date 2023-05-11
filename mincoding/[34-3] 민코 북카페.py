N = int(input())
books = list(input().split())
books.sort()  # 사전 순 정렬

def binary(arr, target, st, ed, cnt):
    # st, ed가 엇갈리거나 시간이 제한시간보다 넘으면 fail
    if st > ed or cnt >= time:
        return 'fail'
    # 이진 탐색
    mid = (st + ed)//2
    if arr[mid] == target:
        return 'pass'
    elif arr[mid] < target:
        return binary(arr, target, mid+1, ed, cnt + 1)
    else:
        return binary(arr, target, st, mid-1, cnt + 1)


M = int(input())
for _ in range(M):
    book, t = input().split()
    time = int(t)
    print(binary(books, book, 0, N-1, 0))