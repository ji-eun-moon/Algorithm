problem = list(input().split('-'))

answer = 0
for i in range(len(problem)):
    nums = list(map(int, problem[i].split('+')))
    if i == 0:
        answer += sum(nums)
    else:
        answer -= sum(nums)

print(answer)