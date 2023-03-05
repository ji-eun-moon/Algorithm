T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 돌아가야할 학생들의 수
    cnt = [0]*200
    for _ in range(N):
        st, ed = map(int, input().split())
        if st > ed:
            st, ed = ed, st
        for i in range((st-1)//2, (ed-1)//2+1):
            cnt[i] += 1

    print(f'#{test_case} {max(cnt)}')
