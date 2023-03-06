for _ in range(4):
    xa, ya, xb, yb, xc, yc, xd, yd = map(int, input().split())

    if xb < xc or xd < xa or yc > yb or ya > yd:
        answer = 'd'
    elif (xb == xc and yb == yc) or (xb == xc and ya == yd) or (xa == xd and ya == yd) or (xa == xd and yb == yc):
        answer = 'c'
    elif xb == xc or xd == xa or ya == yd or yc == yb:
        answer = 'b'
    else:
        answer = 'a'

    print(answer)