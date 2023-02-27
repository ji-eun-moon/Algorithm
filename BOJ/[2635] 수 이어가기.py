N = int(input())  # 첫번째 수
Max = 0
for i in range(1, N+1):  # 두 번째 수 고르기 (1부터 N이하까지)
    lst = [N]
    lst.append(i)
    while True:
        lst.append(lst[-2] - lst[-1])
        if lst[-1] < 0:
            lst.pop(-1)
            break
    if Max < len(lst):
        Max = len(lst)
        answer = lst

print(len(answer))
print(*answer)