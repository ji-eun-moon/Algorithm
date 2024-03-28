'''
https://www.acmicpc.net/problem/3020

- 장애물은 번갈아가면서
- 개똥벌레가 파괴해야 하는 장애물의 최솟값과 구간의 개수
- O(N)으로 풀어야 함
'''

N, H = map(int, input().split())  # 길이, 높이
up = [0] * (H+1)  # 높이 i 에서 잘리는 종유석
down = [0] * (H+1)  # 높이 i에서 잘리는 석순

# 장애물의 크기 입력
for i in range(N):
    height = int(input())
    if i % 2 == 0:
        down[height] += 1
    else:
        up[height] += 1

# 인덱스를 역순으로 누적합을 계산
for i in range(H-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min_count = N
same_height = 0

for h in range(1, H+1):
    if min_count > down[h] + up[H-h+1]:
        min_count = down[h] + up[H-h+1]
        same_height = 1
    elif min_count == down[h] + up[H-h+1]:
        same_height += 1

print(min_count, same_height)