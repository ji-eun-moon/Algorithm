T = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(T):
    A, B = map(int, input().split())
    lcm = A * B // gcd(A, B)
    print(lcm)