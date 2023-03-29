T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # 컨테이너 개수, 트럭 개수
    W = list(map(int, input().split()))  # 화물 무게 (N개)
    T = list(map(int, input().split()))  # 트럭 용량 (M개)

    # 내림차순 정렬
    W.sort(reverse=True)
    T.sort(reverse=True)

    result = 0
    t = 0  # 트럭 인덱스
    for i in range(N):
        # 트럭 전부 확인했으면 break
        if t == M:
            break
        # 트럭 용량이 화물 무게보다 크면 무게 더하고 다음 트럭에 담을것 확인하기
        if T[t] >= W[i]:
            result += W[i]
            t += 1
        else:
            continue

    print(f'#{test_case} {result}')



