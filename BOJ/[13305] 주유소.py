N = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
cost = price[0]
for i in range(N-1):  # 간선의 개수 만큼
    cost = min(cost, price[i])
    result += cost * distance[i]

print(result)