# Solution 1
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()  # 당근 오름차순 정렬

    Min = 21e8
    for i in range(N-2):  # 소 박스
        for j in range(i+1, N-1):  # 중박스
            # 같은 크기가 다른 박스에 들어가는 경우 제외
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                # A, B, C 소, 중, 대 당근의 개수
                A = i + 1
                B = j - i
                C = N - 1 - j
                # 빈박스이거나 한 상자에 N/2개 초과해서 들어가면 안됨
                if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                    if Min > (max(A, B, C) - min(A, B, C)):
                        Min = (max(A, B, C) - min(A, B, C))

    if Min == 21e8:
        Min = -1

    print(f'#{test_case} {Min}')

# Solution 2
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    size = [0]*31  # 당근의 크기 1 ~ 30
    for c in arr:  # 크기별로 개수 파악
        size[c] += 1

    Min = 21e8
    for i in range(29):  # 소박스 마지막 크기 1 ~ 28
        for j in range(30):  # 중박스 마지막 크기 i+1 ~ 29
            A = sum(size[1:i+1])
            B = sum(size[i+1:j+1])
            C = sum(size[j+1:31])
            if A * B * C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:
                diff = (max(A, B, C) - min(A, B, C))
                if Min > diff:
                    Min = diff

    if Min == 21e8:
        Min = -1

    print(f'#{test_case} {Min}')