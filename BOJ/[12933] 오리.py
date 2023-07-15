# sound = input()  # 녹음한 소리
# N = len(sound)
#
# lst = []
# for i in range(N):
#
#     if sound[i] == 'q':
#         if len(lst) == 0:
#             lst.append(['q'])
#         else:
#             for a in lst:
#                 if ''.join(a) == 'quack':
#                     lst.remove(a)
#                     lst.append(['q'])
#                     break
#             else:
#                 lst.append(['q'])
#
#     elif sound[i] == 'u':
#         flag = 0
#         for a in lst:
#             if len(a) == 1 and a[-1] == 'q':
#                 a.append('u')
#                 flag = 1
#                 break
#         if flag == 0:
#             break
#
#     elif sound[i] == 'a':
#         flag = 0
#         for a in lst:
#             if len(a) == 2 and a[-1] == 'u':
#                 a.append('a')
#                 flag = 1
#                 break
#         if flag == 0:
#             break
#
#     elif sound[i] == 'c':
#         flag = 0
#         for a in lst:
#             if len(a) == 3 and a[-1] == 'a':
#                 a.append('c')
#                 flag = 1
#                 break
#         if flag == 0:
#             break
#
#     elif sound[i] == 'k':
#         flag = 0
#         for a in lst:
#             if len(a) == 4 and a[-1] == 'c':
#                 a.append('k')
#                 flag = 1
#                 break
#         if flag == 0:
#             break
#
# if lst:
#     cnt = 0
#     for a in lst:
#         if ''.join(a) == 'quack':
#             cnt += 1
#         else:  # 울다 만 소리가 있는지 확인하기 위해
#             print(-1)
#             break
#     else:
#         print(cnt)
# else:
#     print(-1)

sound = input()
N = len(sound)
visited = [0] * N
duck = 'quack'

def find(start):
    global cnt
    j = 0  # 오리 울음 소리 비교할 index
    flag = 0
    for i in range(start, N):
        if sound[i] == duck[j] and not visited[i]:  # quack 확인하기
            visited[i] = 1
            if sound[i] == 'k':  # 끝까지 울었으면
                if flag == 0:  # flag 안켜져 있을 때만 오리 카운트
                    cnt += 1  # 오리 수 + 1
                    flag = 1  # flag 켜기
                j = 0  # 다시 q 부터 비교하기 위해
            else:  # 끝까지 안울었으면 울음소리 인덱스 + 1
                j += 1

if len(sound) % 5:  # sound가 5의 배수가 아니라면 -1 출력
    print(-1)
else:
    cnt = 0
    for i in range(N):  # 오리 찾기
        if sound[i] == 'q' and visited[i] == 0:
            find(i)
    if cnt == 0 or not all(visited):  # 오리가 없거나 확인하지 않은 인덱스가 있다면 -1 출력
        print(-1)
    else:  # 오리 수 출력
        print(cnt)