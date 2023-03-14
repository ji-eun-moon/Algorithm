# 풀이중
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # 화덕 크기, 피자 개수
    pizza = list(map(int, input().split()))  # 피자에 뿌려진 치즈의 양
    idx = list(range(1, M+1))  # 피자 번호

    # N개의 피자 오븐에 넣기
    oven = []
    for i in range(N):
        temp1 = idx.pop(0)
        temp2 = pizza.pop(0)
        oven.append((temp1, temp2))  # 피자번호, 인덱스

    while True:
        # 오븐에 피자가 하나만 남으면 break
        if len(oven) == 1:
            break
        # 오븐에 아직 공간이 있고, 피자가 남아 있으면 오븐에 추가하기
        if len(oven) < N and pizza:
            temp1 = idx.pop(0)
            temp2 = pizza.pop(0)
            oven.append((temp1, temp2))
        # 치즈꺼내서 확인하고 안녹았으면 다시 넣기
        i, inpizza = oven.pop(0)
        if inpizza//2 != 0:
            oven.append((i, inpizza//2))
        else:
            continue

    print(f'#{test_case} {oven[0][0]}')