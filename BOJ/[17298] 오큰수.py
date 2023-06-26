N = int(input())
lst = list(map(int, input().split()))
ans = [0] * N
stack = []

for i in range(N):
    # 스택이 비어있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while stack and lst[stack[-1]] < lst[i]:
        ans[stack.pop()] = lst[i]  # 정답리스트에 오큰수를 현재 수열로 저장
    stack.append(i)

# 반복문 다 돌았는데 스택이 비어있지 않다면 빌 때까지 -1 로 채우기
while stack:
    ans[stack.pop()] = -1

print(*ans)