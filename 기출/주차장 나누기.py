def solution(n, cars, links):
    cars = [0] + cars
    # 그래프 초기화
    graph = {i : [] for i in range(1, n+1)}

    for u, v in links:
        graph[u].append(v)
        graph[v].append(u)

    visited = [0]*(n+1)
    visited[1] = 1
    stack = [1]

    while stack:

        # 인접한 노드(자식 노드)가 있는 경우
        if graph[stack[-1]]:
            # 방문하지 않은 자식 노드 스택에 담기
            tmp = graph[stack[-1]].pop()
            if not visited[tmp]:
                visited[tmp] = 1
                stack.append(tmp)

        # 자식 노드가 없는 경우 - 가장 마지막 자식
        else:
            tmp = stack.pop()
            # 꺼내고 난 후 스택 가장 위에 있는 것이 부모 노드이므로,
            # 부모노드에 해당 노드 값 더함
            if stack:
                cars[stack[-1]] += cars[tmp]

    total = cars[1]
    answer = float('inf')
    for sub_sum in cars:
        answer = min(answer, abs(total - 2 * sub_sum))
    return answer



print(solution(13,[22,9,1,15,8,6,20,7,11,5,10,4,1],[[4,7],[13,10],[6,3],[7,1],[6,12],[5,11],[5,6],[5,10],[9,8],[8,11],[8,2],[7,8]]))