# import sys
# input = sys.stdin.readline
#
# N = int(input())
# M = int(input())
# lst = list(input())
# n = M - (2*N+1) + 1
#
# def check(idx):
#     for j in range(2*N+1):
#         if j % 2 == 0:
#             if lst[j+idx] != 'I':
#                 return 0
#         else:
#             if lst[j+idx] != 'O':
#                 return 0
#     return 1
#
# cnt = 0
# for i in range(n):
#     if lst[i] == 'I':
#         if check(i):
#             cnt += 1
#
# print(cnt)

N = int(input())
M = int(input())
S = input()

cursor, count, result = 0, 0, 0

while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI': #3칸
        count += 1
        cursor += 2
        if count == N:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(result)