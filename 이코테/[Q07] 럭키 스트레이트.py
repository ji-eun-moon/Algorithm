N = list(map(int, input()))

sum_left = 0
sum_right = 0

for i in range(len(N)):
    if 0 <= i < len(N)//2:
        sum_left += N[i]
    else:
        sum_right += N[i]

if sum_left == sum_right:
    print('LUCKY')
else:
    print('READY')
