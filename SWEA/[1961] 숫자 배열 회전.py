def move_90(arr):  # 오른쪽으로 90도 회전하는 함수
    move_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            move_90[j][N-i-1] = arr[i][j]
    return move_90

T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    result = [[0]*3 for _ in range(N)]

    for i in range(3):
        arr = move_90(arr)  # 90도 회전하고 결과값 result 배열에 넣기
        for j in range(N):
            result[j][i] = ''.join(arr[j])

    print(f'#{test_case}')

    for a in result:
        for b in a:
            print(b, end=' ')
        print()