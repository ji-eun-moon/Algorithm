# N = int(input())
#
# # 감소하는 수인지 확인
# def check(num):
#     num_str = str(num)
#     n = len(num_str)
#     for i in range(1, n):
#         if int(num_str[i]) >= int(num_str[i-1]):
#             return False
#     return True
#
# def find(N):
#     num = 0
#     level = 0
#     while True:
#         if num > 9876543210:
#             return -1
#         if check(num):
#             if level == N:
#                 return num
#             level += 1
#         num += 1
#
# print(find(N))

N = int(input())
result = []

def dfs(level, start, n):
    number = range(0, 10)
    if level == n:
        num = path[:]
        num.sort(reverse=True)  # 감소하는 수로 만들고
        result.append(''.join(map(str, num)))  # 그 수를 결과 리스트에 넣기
        return
    for i in range(start, 10):
        path[level] = number[i]
        dfs(level+1, i+1, n)
        path[level] = 0

# 최대 감소하는 수 = 9876543210 -> 10자리
# 1 ~ 10자리에 대하여 0 ~ 9 숫자를 뽑아 만들 수 있는 조합을 만든다.
for i in range(1, 11):
    path = [0]*i
    dfs(0, 0, i)

result.sort(key=lambda x:(len(x), x))  # 결과리스트 오름차순 정렬 (길이 우선, 그 다음 크기 순)
if N >= len(result):  # N이 인덱스 초과하면 -1 출력
    print(-1)
else:  # 그렇지 않으면 결과 출력
    print(result[N])

