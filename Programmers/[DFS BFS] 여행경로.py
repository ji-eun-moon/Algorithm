tickets = [["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]
def solution(tickets):
    N = len(tickets)
    dic = {}
    answer = []

    for ticket in tickets:
        dic.setdefault(ticket[0], [])
        dic[ticket[0]] = ticket[1]

    def bfs():
        used = [0] * N
        temp = []
        q = []
        q.append(['ICN'])
        while q:
            st = q.pop(0)

            # 갈 수 있는 도착지 없으면 continue
            if dic.get(st) == None:
                continue
            print(temp)
            ed = dic[st]
            # 표 인덱스 찾기
            for i in range(N):
                if tickets[i] == [st, ed]:
                    idx = i

            # 티켓 전부다 확인했는지 체크하고 answer에 넣기
            if len(temp) == N:
                answer.append(temp)

            if used[idx] == 0:
                used[idx] = 1
                q.append(ed)

            temp.append(dic[st])


        return temp


    answer.sort()

    return bfs()

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