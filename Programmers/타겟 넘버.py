numbers = list(map(int, input().split()))
target = int(input())

answer = 0
def dfs(level, Sum):
    global answer
    if level == len(numbers):
        if Sum == target:
            answer += 1
        return
    dfs(level+1, Sum + numbers[level])
    dfs(level+1, Sum - numbers[level])

def solution(numbers, target):
    dfs(0, 0)
    return answer

print(solution(numbers, target))