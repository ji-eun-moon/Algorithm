a, b, c = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def solve(a, b):
    ret = [0] * 2
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a // b
    v = solve(b, a % b)
    ret[0] = v[1]
    ret[1] = v[0] - v[1] * q
    return ret


if c % gcd(a, b) != 0:
    print(-1)
else:
    k = int(c / gcd(a, b))
    ret = solve(a, b)
    print(ret[0]*k, ret[1]*k)

