N = int(input())
cnt = 0
start = 1
end = 1
Sum = 1
while True:
    if end == N:
        cnt += 1
        break
    if Sum == N:
        cnt += 1
        end += 1
        Sum += end
    elif Sum > N:
        Sum -= start
        start += 1
    else:
        end += 1
        Sum += end

print(cnt)