N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(N):
    num = arr[i]
    st = 0
    ed = N-1
    while st < ed:
        Sum = arr[st] + arr[ed]
        if Sum < num:
            st += 1
        elif Sum > num:
            ed -= 1
        else:
            if st != i and ed != i:
                answer += 1
                break
            elif st == i:
                st += 1
            elif ed == i:
                ed -= 1

print(answer)