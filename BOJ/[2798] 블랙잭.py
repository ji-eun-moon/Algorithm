N, M = map(int, input().split())
lst = list(map(int, input().split()))

ret = 21e8
for i in range(N):
    a = lst[i]
    for j in range(i+1, N):
        b = lst[j]
        for k in range(j+1, N):
            c = lst[k]
            Sum = a + b + c
            if abs(Sum - M) < ret and Sum <= M:
                ret = abs(Sum - M)
                answer = Sum

print(answer)