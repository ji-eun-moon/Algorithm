# Solution 1
T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time = sorted(arrive_time)

    result = 'Possible'
    # 손님이 도착한 시간에 만들 수 있는 붕어빵 개수가 필요한 붕어빵개수보다 작을 경우 Impossible
    for i in range(N):
        make = (arrive_time[i]//M) * K
        if make - (i+1) < 0:
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')


# Solution 2
T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))

    result = 'Possible'
    # 시간 테이블 생성하고 arrive_time 테이블을 돌면서 해당 시간에 필요한 붕어빵 수 세기
    time_dat = [0]*11112
    for i in range(N):
        time_dat[arrive_time[i]+1] += 1

    # 필요한 붕어빵 수 누적 합
    for i in range(1, 11111):
        time_dat[i+1] += time_dat[i]

    # 시간 테이블 돌며 필요한 그 시간에 붕어빵 수보다 적게 만들면 Impossible
    # M초에 K개 => i초에 (i//M)*K개
    for i in range(11112):
        if (i//M)*K - time_dat[i] < 0:
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')