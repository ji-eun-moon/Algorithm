# DFS
def solution(N, computers):

    visited = [0]*N

    def dfs(node):
        # 함수 진입시 방문 체크
        visited[node] = 1
        for i in range(N):
            # 연결된 노드이고 아직 방문하지 않았으면 dfs 탐색
            if computers[node][i] == 1:
                if visited[i] == 0:
                    dfs(i)

    answer = 0
    for i in range(N):
        if visited[i] == 0:  # 아직 확인하지 않은 노드이면
            dfs(i)  # dfs 탐색
            answer += 1  # 네트워크 +1

    return answer

# Union Find
def solution(N, computers):

    # arr에 0이 저장되어 있으면 boss
    arr = [0]*N

    def findboss(member):
        # 자기 자신이 boss 라면 자기 자신 return
        if arr[member] == 0:
            return member
        ret = findboss(arr[member])
        return ret

    # 그룹화
    def setunion(a, b):
        # 보스 찾기
        fa, fb = findboss(a), findboss(b)
        # 각각의 보스가 같으면 이미 같은 그룹
        if fa == fb:
            return
        # 다르다면 b 보스에 a 보스 각인
        arr[fb] = fa

    for y in range(N):
        for x in range(N):
            # 연결되어 있는 노드이면 그룹화하기
            if computers[y][x] == 1:
                setunion(y, x)
                print(arr)

    # arr에 저장된 0의 개수(boss의 수)가 최종 그룹의 수
    answer = 0
    for i in range(N):
        if arr[i] == 0:
            answer += 1

    return answer
