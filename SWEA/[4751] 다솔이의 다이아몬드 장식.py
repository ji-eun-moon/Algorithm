T = int(input())
for test_case in range(1, T + 1):
    word = list(input())
    N = 5 + 4*(len(word)-1)  # 열의 개수
    arr = [['.']*N for _ in range(5)]

    for i in range(5):
        for j in range(N):
            if i % 2 == 0 and (j-2) % 4 == 0:
                arr[i][j] = '#'
            if i % 2 and j % 2:
                arr[i][j] = '#'
            if i == 2 and j % 4 == 0:
                arr[i][j] = '#'


    for i in range(len(word)):
        arr[2][2+4*i] = word[i]

    for a in arr:
        for b in a:
            print(b, end='')
        print()