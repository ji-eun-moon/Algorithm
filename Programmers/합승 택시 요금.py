'''
n = 지점의 개수
s = 출발 지점
a = A의 도착지
b = B의 도착지
fares[i] = 지점 사이의 예상 택시 요금 : [지점 1, 지점 2, 택시 요금] (무방향)
* A, B 두 사람이 s 에서 출발해서 각각의 도착 지점까지 택시 타고 갈때 최저 예상 요금?
1. s -> a, s -> b
2. s -> x -> a, s -> x -> b
'''

import heapq
def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]

    # 무방향 그래프 만들기
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 다익스트라 알고리즘
    def dijkstra(graph, start, end):
        distance = [float("inf")] * (n+1)
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for vv, ww in graph[now]:
                cost = distance[now] + ww
                if cost < distance[vv]:
                    distance[vv] = cost
                    heapq.heappush(q, (cost, vv))

        return distance[end]

    # s -> x -> a, s -> x -> b 의 최소 비용
    answer = float("inf")
    for i in range(1, n+1):
        # 합승 하는 경우 : s -> x, x -> a, x -> b
        tmp1 = dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b)
        # 합승 안하는 경우 : s -> a, s -> b : 어차피 tmp1 에 포함되므로 생략 가능
        # tmp2 = dijkstra(graph, s, a) + dijkstra(graph, s, b)
        # 최소 비용 계산
        answer = min(answer, tmp1)

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))