N = int(input())
answer = 0
# arr[r] = c -> r행 c열에 퀸이 있음
arr = [0]*N

# 퀸 자리가 유효한지 체크하는 함수
def queen(r):
    for i in range(r):
        # 세로 체크(열이 같을 때)
        if arr[i] == arr[r]:
            return 0
        # 대각선 체크(행과 열이 같을 때)
        if abs(r-i) == abs(arr[r]-arr[i]):
            return 0
    return 1

# r 행에 퀸 놓는 함수
def dfs(r):
    global answer
    # 퀸을 N행 까지 조건에 맞게 다 채워 넣으면 answer +1 하고 리턴
    if r == N:
        answer += 1
        return
    for i in range(N):
        arr[r] = i  # r행 i열에 퀸을 놓기
        if queen(r) == 1:  # 해당 자리에 놓을 수 있다면
            dfs(r+1)  # 다음행으로 넘어가기


dfs(0)
print(answer)