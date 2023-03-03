W, H = map(int, input().split())
p, q = map(int, input().split())  # 개미 초기 좌표(x, y)
t = int(input())

x = (p + t) % W if ((p+t)//W) % 2 == 0 else W - ((p + t) % W)
y = (q + t) % H if ((q+t)//H) % 2 == 0 else H - ((q + t) % H)
# 풀어 쓰면
# if ((p+t)//W) % 2 == 0:
#     x = (p + t) % W
# else:
#     x = W - ((p + t) % W)
#
# if ((q+t)//H) % 2 == 0:
#     y = (q + t) % H
# else:
#     y = H - ((q + t) % H)

print(x, y)