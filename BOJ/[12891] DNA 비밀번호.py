S, P = map(int, input().split())  # 임의로 만든 문자열, 비밀번호로 사용할 문자열 길이
st = input()
dic = {}
A, C, G, T = map(int, input().split())
dic['A'], dic['C'], dic['G'], dic['T'] = A, C, G, T
cnt = 0
# 시간 초과
# for i in range(S-P+1):
#     check = copy.deepcopy(dic)
#     for j in range(i, i+P):
#         check[st[j]] -= 1
#     if check['A'] <= 0 and check['C'] <= 0 and check['G'] <= 0 and check['T'] <= 0:
#         cnt += 1
# print(cnt)


# 초기 조건
for i in range(P):
    dic[st[i]] -= 1
if dic['A'] <= 0 and dic['C'] <= 0 and dic['G'] <= 0 and dic['T'] <= 0:
    cnt += 1

for j in range(S-P):
    dic[st[j]] += 1
    dic[st[j+P]] -= 1
    if dic['A'] <= 0 and dic['C'] <= 0 and dic['G'] <= 0 and dic['T'] <= 0:
        cnt += 1

print(cnt)

