N = int(input())  # 재료의 개수
M = int(input())  # 갑옷을 만드는데 필요한 수
arr = list(map(int, input().split()))  # 갑옷이 가지는 고유한 번호
arr.sort()

answer = 0

st = 0
ed = N-1
while st < ed:
    if arr[st] + arr[ed] < M:
        st += 1
    elif arr[st] + arr[ed] > M:
        ed -= 1
    else:
        answer += 1
        st += 1

print(answer)