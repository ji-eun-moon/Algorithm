# A = list(input())
# B = list(input())
# A.sort()
# B.sort()
#
# def check(A, B):
#     if len(A) != len(B):
#         return 'anagram 아님'
#     else:
#         for i in range(len(A)):
#             if A[i] != B[i]:
#                 return 'anagram 아님'
#         return 'anagram'
#
# print(check(A, B))

# 문자열 2개를 입력 받고 입력 시 최소 몇개의 글자를 지우면 두 문자열이 anagram이 되나요?!

A = list(input())
B = list(input())

dic = {}
for i in range(len(A)):
    dic.setdefault(A[i], 0)
    dic[A[i]] += 1

for i in range(len(B)):
    dic.setdefault(B[i], 0)
    dic[B[i]] -= 1

cnt = 0
for value in dic.values():
    if value != 0:
        cnt += abs(value)

print(cnt)

# 문자열 2개 입력 받은 후 arr2의 연속된 부분 문자열 중 arr1의 아나그램 개수 출력 (arr1의 문자열의 길이가 arr2의 길이보다 짧다)
arr1 = input()
arr2 = input()
