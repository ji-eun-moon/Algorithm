from heapq import heappush, heappop

def solution(n, paths, gates, summits):

    summits.sort()
    summit_set = set(summits)

    # 무방향 그래프 만들기
    graph = {}
    for i, j, w in paths:
        graph.setdefault(i, [])
        graph.setdefault(j, [])
        graph[i].append((j, w))
        graph[j].append((i, w))

    heap = []
    visited = [10000001] * (n + 1)

    # 모든 출입구를 우선순위큐에 삽입
    for gate in gates:
        heappush(heap, (gate, 0))
        visited[gate] = 0

    # 다익스트라 알고리즘
    while heap:
        node, intensity = heappop(heap)

        if intensity > visited[node] or node in summit_set:
            continue

        for next_node, weight in graph[node]:
            # 가중치의 최댓값 구하기
            next_intensity = max(weight, intensity)
            # 각 노드에 도달하는 과정의 최대 intensity 값 저장
            if next_intensity < visited[next_node]:
                visited[next_node] = next_intensity
                heappush(heap, (next_node, next_intensity))

    # 다익스트라 완료 후 산봉우리들을 순회하며 정답 찾기
    min_intensity = [0, 10000001]  # 산봉우리, intensity
    for summit in summits:
        if min_intensity[1] > visited[summit]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]

    return min_intensity

print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))