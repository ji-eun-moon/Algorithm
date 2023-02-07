T = 10
for test_case in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 방향 배열 생성
    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, 1, -1]
    
    # 기준좌표 상,하,좌,우로 이웃한 요소와의 차의 절대값들의 합 구하는 함수
    def getSum(y, x):
        ret = 0  # 절대값의 합 변수 초기화
        for a in range(4):
            dy = y + direct_y[a]
            dx = x + direct_x[a]
            if dy < 0 or dy >= N or dx < 0 or dx >= N:  # 방향 좌표가 범위 벗어나는 경우 continue
                continue
            ret += abs(arr[y][x]-arr[dy][dx])  # 결과를 절대값들의 합 변수에 더함
        return ret
 
    ans = 0  # 최종 합 변수 초기화
    for i in range(N):
        for j in range(N):  # N x N 배열 원소를 하나씩 돌며
            result = getSum(i, j)  # getSum 함수 실행
            ans += result  # 결과를 최종 합 변수에 더함
 
    print(f'#{test_case} {ans}')