tickets = [["ICN", "AAA"], ["BBB", "ICN"], ["ICN", "BBB"]]
def solution(tickets):
    global path, answer
    N = len(tickets)
    answer = []

    # ICN ticket 찾기 - 시작
    icn = []
    for i in range(N):
        if tickets[i][0] == 'ICN':
            idx = i
            icn.append(idx)

    def dfs(idx):
        global path, answer
        # 출발지, 도착지
        st = tickets[idx][0]
        ed = tickets[idx][1]
        # path 배열의 길이가 N이면 티켓을 끝까지 사용하는 것을 성공했으므로 answer 배열에 담기
        # 이 때 마지막 ed가 안담겨있으므로 추가해주어야 함
        if len(path) == N:
            answer.append(path[:]+[ed])
            return
        for i in range(N):
            # 아직 사용하지 않은 티켓이고 티켓의 도착지와 다음 티켓의 출발지가 같다면
            if used[i] == 0 and tickets[i][0] == ed:
                path.append(ed)
                used[i] = 1
                dfs(i)
                path.pop()
                used[i] = 0

    # 가능한 시작 지점 전부 탐색, 탐색할때마다 used, path 배열 초기화
    for i in range(len(icn)):
        used = [0] * N
        idx = icn[i]
        used[idx] = 1
        path = ['ICN']
        dfs(idx)

    # 알파벳 순으로 정렬
    answer.sort()
    # 가장 앞에꺼가 정답
    return answer[0]

print(solution(tickets))


# 오답
# def solution(tickets):
#     N = len(tickets)
#     answer = []
#     # 도착지 기준 알파벳 오름차순으로 정렬하기
#     tickets = sorted(tickets, key=lambda x: x[1])
#
#     # ICN ticket 찾기
#     # 출발지가 없는 티켓이 있다면 continue
#     icn = []
#     for i in range(N):
#         if tickets[i][0] == 'ICN':
#             idx = i
#             icn.append(idx)
#
#     def bfs():
#         used = [0] * N
#         temp = []
#         q = []
#         q.append(tickets[idx])
#         used[idx] = 1
#         while q:
#             st, ed = q.pop(0)
#             temp.append(st)
#             for i in range(N):
#                 if used[i] == 0 and ed == tickets[i][0]:
#                     used[i] = 1
#                     q.append(tickets[i])
#                     break
#         temp.append(ed)
#         return temp
#
#     for i in range(len(icn)):
#         idx = icn[i]
#         path = bfs()
#         if len(path) == N + 1:
#             answer.append(path)
#
#     answer.sort()
#
#     return answer[0]