N, K = map(int, input().split())  # 물병의 개수, 만들어야 하는 물병 수
cnt = 0
# 이진수의 개수 = 물병의 개수
while bin(N).count('1') > K:
    # 물병의 개수가 K 이하가 될 때까지 반복문 실행
    N += 1
    cnt += 1
print(cnt)