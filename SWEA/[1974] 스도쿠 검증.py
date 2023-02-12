T = int(input())

def checkG(y):
    for i in range(9):
        if arr[y][i] not in lst:
            return 0
        lst.remove(arr[y][i])
    return 1

def checkS(x):
    for i in range(9):
        if arr[i][x] not in lst:
            return 0
        lst.remove(arr[i][x])
    return 1

def checkR(y, x):
    for i in range(3):
        for j in range(3):
            if arr[y+i][x+j] not in lst:
                return 0
            lst.remove(arr[y+i][x+j])
    return 1

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = 0
    for y in range(9):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if checkG(y) == 1:
            flag += 1

    for x in range(9):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if checkS(x) == 1:
            flag += 1

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if checkR(i, j) == 1:
                flag += 1

    if flag == 27:
        ans = 1
    else:
        ans = 0

    print(f'#{test_case} {ans}')