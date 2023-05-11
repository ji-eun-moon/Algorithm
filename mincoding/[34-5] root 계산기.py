N = int(input())

def root(num, st, ed):
    if st > ed:  # 안적어주면 입력 값이 음수인 경우 무한 루프
        return 'fail'
    mid = (st + ed) // 2
    if mid * mid <= num < (mid + 1) * (mid + 1):
        return mid
    elif num < mid * mid:
        return root(num, st, mid - 1)
    else:
        return root(num, mid + 1, ed)

print(root(N, 0, N))